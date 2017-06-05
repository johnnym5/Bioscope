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
		return render_template('home.html', user = "demo", posts = lst, genres = getGenres(), selectedGenre = "Action", movies = getMoviesByGenre('Action'))
		#if session.get('user'):
			#data = session.get('user')
			#return render_template('home.html', user = data[0][2])
		#else:
			#return 'Session error'
	
	except Exception as e:
		return "Error at /home" + str(e)
	
# App route to browse by movie Genre
@app.route('/browseByGenre', methods = ['POST'])
def browseByGenre():
	try:
		genre = request.form['genre']
		#return json.dumps(getMoviesByGenre(str(genre)))
		
		return render_template('home.html', user = "demo", posts = getTopTen() , genres = getGenres(), selectedGenre = str(genre), movies = getMoviesByGenre(str(genre)))
	
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
	


# ---------------------------------------------------------------------
#															KITTENS
# ---------------------------------------------------------------------

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
			
	
# ---------------------------------------------------------------------
#												MAIN
# ---------------------------------------------------------------------
			
# App launches here
if __name__ == "__main__":
    app.run(debug=True)
		#http_server = WSGIServer(('', 5000), app)
		#http_server.serve_forever()