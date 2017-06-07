# This file constitutes the starting point and app routes. Queries, #and
# app configurations are all included in this file.
#
# @version  : 1.0.0
# @author 	: Dev Team via BioScope
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
#														IMPORTS
# ---------------------------------------------------------------------

from flask import Flask, render_template, request, json, redirect, session, url_for, jsonify, get_template_attribute
import MySQLdb
import time
from werkzeug import generate_password_hash, check_password_hash

# ---------------------------------------------------------------------
#												APP CONFIGURATION
# ---------------------------------------------------------------------

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'movierRental'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = 'bolbbalgan4'

# ---------------------------------------------------------------------
#											DATABASE CONNECTION
# ---------------------------------------------------------------------

conn = MySQLdb.connect("localhost", "root", "root", "movieRental")
cursor = conn.cursor()

# ---------------------------------------------------------------------
#													APP ROUTES
# ---------------------------------------------------------------------


# App route for starting point (index)
@app.route('/')
def main():
	return render_template('index.html')

# App route for showing signUp page
@app.route('/signUp')
def signUp():
	return render_template('signUp.html')

# App route for sending signup data
@app.route('/signUpUser', methods=['POST', 'GET'])
def signUpUser():
		error = 0
		try:
			_fname = request.form['fn']		# first name
			_lname = request.form['ln']		# last name
			_email = request.form['em']		# email
			_pwd = request.form['pwd']		# password, to be hashed later
			_type = request.form['optradio'] # type of account
			_sa = request.form['sa']			# street address
			_ct =  request.form['ct']			# city 
			_st = request.form['st']			# state
			_zip = request.form['zip']		# zipCode
			_tel = request.form['tel']		# Telephone
			_cc = request.form['cc']			# Credit Card
		
			_hash = generate_password_hash(_pwd)
			
			query = "INSERT INTO Customers(lastName, firstName, Email, hashPassword, AccountType, Address, City, State, ZipCode, CreditCard, Telephone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			
			
			args = (_lname, _fname, _email, _pwd, _type, _sa, _ct, _st, _zip, _cc, _tel)
    
			cursor.execute(query, args)
			data = cursor.fetchall()
			
			if len(data) is 0:
				conn.commit()
				
			else:
				error = 1
			setUpCustomer(str(_email), str(_type)) # Update accounts table
			
		except Exception as e:
			print e
			error = 1
		
		finally:
			#cursor.close()
			#conn.close()
			if(error == 0):
				return render_template('signIn.html')
			else:
				return 'ERROR'

# App route to Sign Users in
@app.route("/SignIn")
def signIn():
	return render_template('signIn.html')
			
# App route to validate users
@app.route("/validateLogin", methods=['POST'])
def validateLogin():
	try:
		logged = False
		_em = request.form['em']
		_pwd = request.form['pwd']
		
		query = ("SELECT * FROM Customers WHERE Email = %s")
		args = (_em,)
		
		data = []
		cursor.execute(query, [_em])
		data = cursor.fetchall()
		
		
		if (len(data) > 0):
			if (_pwd == str(data[0][10])):
				session['user'] = data
				logged = True
				
	except Exception as e:
		print e
		
	finally:
		if(logged):
			return redirect(url_for('home'))
		else:
			return render_template('signIn_error.html')
			
# App home page after user has signed in
@app.route('/home')
def home():
	try:
		lst =  getTopTen()
		#return str(post)
		#return render_template('home.html', user = "demo", posts = lst, genres = getGenres(), selectedGenre = "Action", movies = getMoviesByGenre('Action'))
		if session.get('user'):
			data = session.get('user')
			return render_template('home.html', user = data[0][2], posts = lst, genres = getGenres(), selectedGenre = "Action", movies = getMoviesByGenre('Action'))
		else:
			return render_template('signIn.html')
	
	except Exception as e:
		return "Error at /home" + str(e)
	
# App route to browse by movie Genre
@app.route('/browseByGenre', methods = ['POST'])
def browseByGenre():
	try:
		genre = request.form['genre']
		#return json.dumps(getMoviesByGenre(str(genre)))
		data = isLoggedIn()
		if data:
			return render_template('home.html', user = data[0][2], posts = getTopTen() , genres = getGenres(), selectedGenre = str(genre), movies = getMoviesByGenre(str(genre)))
		else:
			return render_template('signIn.html')
	
	except Exception as e:
		return "Error at /browseByGenre: " + str(e)

# App route to search movies and actors
@app.route('/search', methods = ['POST'])
def search():
	try:
		categ = request.form['optradio']  # Movie or actor
		terms = request.form['search']		# Search terms

		if (categ == "Movie"):
			# get all the movies
			tmp = searchMovies(str(terms))
			if tmp == "Empty Query":
				title = "Sorry, there were no results for " + terms
				return render_template('search.html', noresults = True, heading  = title)
			else:
				title = "Movie results for " + terms
				return render_template('search.html', user = 'demo', heading = title, results = tmp)
			
		else:
			# Search by actors
			tmp = searchActors(str(terms))
			if tmp == "Empty Query":
				title = "Sory, there were no results for " + terms
				return render_template('search.html', noresults = True, heading  = title)
			else:
				title = "Movie results for " + terms
				return render_template('search.html', user = 'demo', heading = title, results = tmp)
	except Exception as e:
		return 'Error at search() ' + str(e)
	
# App route to view a selected movie
@app.route('/movie', methods = ['POST'])
def movie():
	Id = request.form['Id']
	tmp = getMovie(str(Id))
	#return str(tmp)
	data = isLoggedIn()
	_check = checkInQueue(data[0][0], str(Id))
	if data:
		return render_template('movie.html', user = data[0][2], check = _check, movie = tmp[0])
	else:
		return render_template('signIn.html')


@app.route('/addToQueue', methods = ['POST'])
def addToQueue():
	try:
		data = session.get('user')
		movieId = request.form['movieId']
		_check = checkInQueue(data[0][0], movieId)
		
		if not (_check):
			query = "INSERT INTO Queue(movieId, CustomerId) VALUES(%s, %s)"
			args = (str(movieId), str(data[0][0]))
			data = []

			cursor.execute(query, args)
			data = cursor.fetchall()

			if (len(data) is 0):
				conn.commit()
				data = isLoggedIn()
				_check = checkInQueue(data[0][0], movieId)
				return render_template('movie.html', user = data[0][2], check = _check, movie = getMovie(str(movieId))[0])
			else:
				return 'Couldnt add to Queue' + str(data)
		else:
			return 'Movie Already in Queue'
		
	except Exception as e:
		return str(e)

@app.route('/queue', methods = ['GET'])
def queue():
	try:
		data = isLoggedIn()
		
		if (len(data) is 0):
			render_template('signIn.html')
		else:
			queue = getQueue(data[0][0])
			if not queue:
				return render_template('queue.html',user = data[0][2], queueEmpty = True)
			else:
				nextIn = queue.pop(0)
				return render_template('queue.html', next = nextIn, queue = queue, user = data[0][2], queueEmpty = False)

	except Exception as e:
		return "Error at /queue : " + str(e)

# App route to rent and remove a movie from the queue	
@app.route('/rentOrRemove', methods = ['POST'])
def rentOrRemove():
	try:
		data = isLoggedIn()
		
		if "remove" in request.form:
			removeFromQueue(data[0][0], str(request.form['_movieId']))
			return redirect(url_for('queue'))
		else:
			# Rent Movie
			return "Rent Movie"
	except Exception as e:
		return "Error at /rentOrRemove: " + str(e)
	
# App route to remove a movie from the queue
@app.route('/removeMovie', methods = ['POST'])
def removeMovie():
	try:
		data = isLoggedIn()
		
		removeFromQueue(data[0][0], str(request.form['movieId']))
		return redirect(url_for('queue'))
	
	except Exception as e:
		return "Error at /removeMovie: " + str(e)
	
@app.route('/test1', methods=['POST'])
def test():
	if "test1" in request.form:
		return "test1"
	else:
		return "test2"

@app.route('/test2')
def test2():
	return ("test2")
# -------------------------------------------------------------------
#															KITTENS
# -------------------------------------------------------------------
# A function to check if a user is logged in
def isLoggedIn():
	return session.get('user')

# A function to add Customer to Accounts and create Query Table
def setUpCustomer(email, act_type):
	try:
		query = "SELECT CustomerId FROM Customers WHERE Email LIKE '%" + email + "%'"
		data = []
		cursor.execute(query)
		data = cursor.fetchall()

		if(len(data) > 0):
			query = "INSERT INTO Accounts(CustomerId, AccountType, CreationDate, LastOrderDate, MoviesRented) VALUES (%s, %s, %s, %s, %s)"
			Id = data[0]
			args = (Id, str(act_type), time.strftime("%d/%m/%Y"), "0", "0")
			
			cursor.execute(query, args)
			data = []
			data = cursor.fetchall()
			if (len(data) is 0):
				conn.commit()
				return str(Id)
			else:
				return 'Error at Insert into Accounts'
			
		else:
			return 'Error at selecting CustomerId from Customers'
	except Exception as e:
		return str(e)

# A function to retrieve top 10 movies
def getTopTen():
	try:
		post = []
		
		query = "SELECT * FROM Movies ORDER BY Rating Desc LIMIT 10"
		data  = []
		cursor.execute(query)
		data = cursor.fetchall()
		
		if (len(data) > 0):
			for row in data:
				#tmp = jsonify()
				post.append({'Id':row[0], 'Director':row[1], 'Duration':row[2], 'Actors':row[3], 'Genre':row[4], 'Title': row[5], 'Rating':row[6], 'Description':row[7], 'Poster': '../static/posters/' + row[0] + '.jpg' })
			return post
		else:
			return 'Error'
	except Exception as e:
		return str(e)
	
# A function populate the genre list
def getGenres():
	genres = [
		'Action',
		'Adventure',
		'Comedy',
		'Drama',
		'Documentary',
		'Fantasy',
		'Family',
		'History',
		'Mystery',
		'Thriller',
		'Romance'
	]
	return genres

# A function to get movies of a certain genre
def getMoviesByGenre(genre):
	try:
		movies = []
		
		query = "SELECT Id, Rating FROM Movies WHERE Genre LIKE " + "'%" + genre + "%'"
		#args = (genre)
		data = []
		cursor.execute(query)
		data = cursor.fetchall()
		
		if (len(data) > 0):
			for row in data:
				movies.append({'Id':row[0], 'Rating':row[1], 'Poster': '../static/posters/' + row[0] + '.jpg'})
			return movies
		else:
			return 'Empty Query'
	
	except Exception as e:
		return 'Error at getMoviesByGenre(): ' + str(e)
	
# A function to search movies by title
def searchMovies(title):
	try:
		movies = []
		
		query = "SELECT Id, Rating FROM Movies WHERE TITLE LIKE " + "'%" + title + "%'"
		data = []
		cursor.execute(query)
		data = cursor.fetchall()
		
		if (len(data) > 0):
			for row in data:
				movies.append({'Id':row[0], 'Rating':row[1], 'Poster': '../static/posters/' + row[0] + '.jpg'})
			return movies
		else:
			return 'Empty Query'
	
	except Exception as e:
		return 'Error at searchMovies(): ' + str(e)

# A function to search Actors by name
def searchActors(title):
	try:
		movies = []
		listed = []
		
		query = "SELECT Movies FROM Actors WHERE Name LIKE " + "'%" + title + "%'"
		data = []
		cursor.execute(query)
		data = cursor.fetchall()
		
		if (len(data) > 0):
			for row in data:
				tmp = row[0].split("|")
				for item in tmp:
					movies.append(item)
		else:
			return 'Empty Query'
		
		data = []
		for movie in movies:
			query = "SELECT Rating FROM Movies WHERE Id LIKE '%" + str(movie) + "%'"
			cursor.execute(query)
			data = cursor.fetchall()
			
			if (len(data) > 0):
				for row in data:
					listed.append({'Id':movie, 'Rating': row[0], 'Poster': '../static/posters/' + movie + '.jpg'})
			else:
				return 'Empty Query'
		
		return listed
	
	except Exception as e:
		return 'Error at searchActors(): ' + str(e)
			
# A function to get a certain movie
def getMovie(Id):
	try:
		movie = []
		query = "SELECT * FROM Movies WHERE Id LIKE '%" + Id + "%'"
		data = []
		cursor.execute(query)
		data = cursor.fetchone()
		
		if(len(data) > 0):
			movie.append({'Id':data[0], 'Director':data[1], 'Duration':data[2], 'Actors':data[3], 'Genre':data[4], 'Title': data[5], 'Rating':data[6], 'Description':data[7], 'Poster': '../static/posters/' + data[0] + '.jpg' })
			return movie
		else:
			return 'Empty Query'
		
	except Exception as e:
		return 'Error at getMovie() :' + str(e)


# A function to see if a movie is already in the queue
def checkInQueue(custId, movieId):
	try:
		query = "SELECT * FROM Queue WHERE (movieId = %s AND CustomerId = %s)"
		data = []
		args = (movieId, custId)
		cursor.execute(query, args)
		data = cursor.fetchall()
		
		if(len(data) is 0):
			return False
		else:
			return True
	except Exception as e:
		return str(e)
	
	
	
# A function to return a Queue owned by a certain user
def getQueue(custId):
	try:
		queue = []
		
		query = "SELECT movieId FROM Queue WHERE CustomerId = %s"
		args = (str(custId))
		cursor.execute(query, args)
		data = cursor.fetchall()
		
		if(len(data) > 0):
			for row in data:
				queue.append({'Id':row[0], 'Poster' : "../static/posters/" + row[0] + ".jpg"})
			return queue
		else:
			return queue
	
	except Exception as e:
		return 'Error at getQueue: ' + str(e)
	
def removeFromQueue(CustId, movieId):
	try:
		query = "DELETE FROM Queue WHERE MovieId = '%s' AND CustomerId = '%s'" %(str(movieId), str(CustId))
		
		cursor.execute(query)
		data = cursor.fetchall()
		
		if (len(data) is 0):
			conn.commit()
			return 'OK'
		else:
			return 'DELETION failed'
	except Exception as e:
		return "Error at removeFromQueue: " + str(e)
	
# -------------------------------------------------------------------
#												MAIN
# -------------------------------------------------------------------			
# App launches here
if __name__ == "__main__":
    app.run(debug=True)
		#http_server = WSGIServer(('', 5000), app)
		#http_server.serve_forever()