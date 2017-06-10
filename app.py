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
import datetime, time
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
@app.route('/index')
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
			return render_template('home.html', user = data[0][2], posts = lst, genres = getGenres(), selectedGenre = "Action", movies = getMoviesByGenre('Action'), sugesstions= suggestions(data[0][0]))
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
	_check = checkInQueue(data[0][0], str(Id))  or checkInOrders(data[0][0], str(Id))
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
				return render_template('queue.html',user = data[0][2], queueEmpty = True, orders = getOrders(str(data[0][0])))
			else:
				nextIn = queue.pop(0)
				return render_template('queue.html', next = nextIn, queue = queue, user = data[0][2], queueEmpty = False, orders = getOrders(str(data[0][0])))

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
			return (rent(str(data[0][0]), str(request.form['_movieId'])))
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
		
	
# An app route to rent a movie
# @app.route('/rent', methods = ['POST'])
def rent(custId, movieId):
	try:
		
		tmp =  rentMovie(custId, movieId)
		if int(tmp) == 0:
			removeFromQueue(custId, movieId)
			return redirect(url_for('queue'))
		else:
			return "Renting rule : " + str(tmp)
	except Exception as e:
		return "Error at rent(): " + str(e)

@app.route('/return', methods=['POST'])
def returnMovie():
	try:
		movieId = request.form	['movieId_']
		data = isLoggedIn()
		returnOrder(data[0][0], movieId)
		return redirect(url_for('queue'))
	except Exception as e:
		return "Error at /returnMovie(): " + str(e)
	
@app.route('/settings')
def settings():
	try:
		data = isLoggedIn()
		
		if (str(data[0][11]) is "limited"):
			limited = True		
		else:
			limited = False
		return render_template('settings.html', fn = str(data[0][2]), ln = str(data[0][1]), limited = limited )
	except Exception as e:
		return 'Error at settings(): ' + str(e)
	
	
@app.route('/changeSettings', methods = ['POST'])
def changeSettings():
	try:
		data = isLoggedIn()
		fn = request.form['fn']
		query = "UPDATE Customers SET FirstName = '%s' WHERE CustomerId = '%s'" %(str(fn), str(data[0][0]))
		cursor.execute(query)
		rep = cursor.fetchall()
		if(len(rep) == 0):
			conn.commit()
			return redirect(url_for('settings'))
		else:
			return 'Empty Query'
	except Exception as e:
		return "Error at changeSettings(): " + str(e)
		
@app.route('/deleteUser', methods = ['POST'])
def deleteUser():
	try:
		data = isLoggedIn()
		query = "DELETE FROM Customers WHERE CustomerId = '%s'" %(str(data[0][0]))
		cursor.execute(query)
		rep = cursor.fetchall()
		if(len(rep) is 0):
			conn.commit()
			session.pop('user', None)
			return redirect(url_for('main'))
		else:
			return str(rep)
	except Exception as e:
		return 'Error at deleteUser()' + str(e)
		

@app.route('/test')
def test():
	data = isLoggedIn()
	return str(suggestions(str(data[0][0])))

@app.route('/logout')
def logout():
	try:
		session.pop('user', None)
		return redirect(url_for('main'))
	except Exception as e:
		return"Error at /logout" + str(e)

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
		query = "SELECT * FROM Queue WHERE movieId = '%s' AND CustomerId = '%s'" % (str(movieId), str(custId))
		data = []
		args = (movieId, custId)
		cursor.execute(query)
		data = cursor.fetchall()
		
		if(len(data) is 0):
			return False
		else:
			return True
	except Exception as e:
		return "error at checkinQueue() :" + str(e)
	
	
	
# A function to return a Queue owned by a certain user
def getQueue(custId):
	try:
		queue = []
		
		query = "SELECT movieId FROM Queue WHERE CustomerId = %s" %(str(custId))
		args = (str(custId))
		cursor.execute(query)
		data = cursor.fetchall()
		
		if(len(data) > 0):
			for row in data:
				queue.append({'Id':row[0], 'Poster' : "../static/posters/" + row[0] + ".jpg"})
			return queue
		else:
			return []
	
	except Exception as e:
		return 'Error at getQueue: ' + str(e)

# A function to remove a movie from the Queue
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
	

# A function to rent a movie
def rentMovie(custId, movieId):
	try:
		data = getAccount(custId)
		if (str(data[1]) == 'limited'):
			if not checkMonth(str(data[3])):	# if true = a month has gone
				if checkCopies(movieId):	
					if(int(str(getMovieCount(custId))) <= 1):
						if not (checkCustomerInOrders(custId)) : # One rent at a time
							# go ahead and rent and increase the movieRent and date
							tmp = lendMovie(custId, movieId)
							return str(tmp)
						else:
							# one rent at a time
							return 100
					else:
						# maximum rents for a month has reached
						return 101
				else:
					# No Copies
					return 102
					
			else:
				# Not a month
				return 103
				#return "Cm: " + checkMonth(str(data[3]))
		else:
			# unlimited plan
			if checkCopies(movieId):
				if not (checkCustomerInOrders(custId)):
					tmp = lendMovie(custId, movieId)
					return str(tmp)
				else:
					return 100
			else:
				return 102
	except Exception as e:
		return "Error at rentMovie(): " + str(e)
	
# A function to complete a rent
def lendMovie(custId, movieId):
	try:
		cnt = int(str(getMovieCount(custId)))
		cnt = cnt + 1
		query = "UPDATE Accounts SET LastOrderDate = '%s', MoviesRented = '%s' WHERE CustomerId = '%s'" %(time.strftime("%d/%m/%Y"), str(cnt), custId)
		cursor.execute(query)
		data = cursor.fetchall()
		
		if(len(data) is 0):
			conn.commit()
			# Update orders
			return updateOrder(custId, movieId)
		else:
			return 'Error updating Accounts'
	except Exception as e:
		return 'Error at lendMovie(): ' + str(e)

# A function to get number of movies rented
def getMovieCount(custId):
	try:
		query = "SELECT MoviesRented FROM Accounts WHERE CustomerId = %s" %(custId)
		args = (custId)
		cursor.execute(query)
		data = cursor.fetchall()
		if (len(data) > 0):
			return data[0][0]
		else:
			return 'Empty Query at getMoviesCount()'
	except Exception as e:
		return 'Error at getMovieCount(): ' + str(e)
	
# A function to update an order
def updateOrder(custId, movieId):
	try:	
		start = datetime.datetime.now().date()
		ret = start + datetime.timedelta(days=3)
		ret = ret.strftime('%d/%m/%Y')
		start = start.strftime('%d/%m/%Y')

		query = "INSERT INTO Orders(CustomerId, MovieId, LendDate, ReturnDate) VALUES (%s, %s, %s, %s)"
		args = (custId, movieId, start, ret)

		cursor.execute(query, args)
		data = cursor.fetchall()

		if(len(data) is 0):
			conn.commit()
			return 0
		else:
			return 'Error inserting into Orders'
	except Exception as e:
		return "Error at updateOrders(): "  + str(e)
		
# A function to check number of copies remaining
def checkCopies(movieId):
	try:
		query = "SELECT Copies FROM Movies WHERE Id = '%s'" %(movieId)
		cursor.execute(query)
		data = cursor.fetchall()
		
		if(len(data) > 0):
			if (data[0][0] > 0):
				return True
			else:
				return False
		else:
			return 'Query Error'
	except Exception as e:
		return "Error at checkCopies() :" + str(e)
	
	
# A function to check if a month has gone = 30 days
def checkMonth(date):
	try:
		if date == "0":
			return False
		else:
			start = datetime.datetime.strptime(str(date), "%d/%m/%Y").date()
			now = datetime.datetime.now().date()
			if ((now-start).days) <= 30:
				return False
			else:
				return True
	except Exception as e:
		return "Error at checkMonth(): " + str(e)
	
# A function to get Account data of a Customer
def getAccount(custId):
	try:
		query = "SELECT * FROM Accounts WHERE CustomerId = '%s'" %(str(custId))
		cursor.execute(query)
		data = cursor.fetchone()

		if(len(data) > 0):
			return data
		else:
			return []
	except Exception as e:
		return "Error at getAccount(): " + str(e)
	
# A function to get orders
def getOrders(custId):
	try: 
		query = "SELECT MovieId, ReturnDate FROM Orders WHERE CustomerId = %s" % (custId)
		args = (custId)
		cursor.execute(query)
		data = cursor.fetchall()
		tmp= []
		if(len(data) > 0):
			for row in data:
				tmp.append({'Id':row[0], 'ReturnDate':row[1], 'Poster': '../static/posters/' + row[0] + '.jpg'})
			return tmp
		else:
			return []
	except Exception as e:
		return "Error at getOrders(): " + str(e)
	
# A function to return an order
def returnOrder(custId, movieId):
	try:
		query = "DELETE FROM Orders WHERE MovieId = '%s' AND CustomerId = '%s'" %(str(movieId), str(custId))
		cursor.execute(query)
		data = cursor.fetchall()
		
		if(len(data) is 0):
			conn.commit()
			return 'OK'
		else:
			return []
	except Exception as e:
		return "Error at returnOrder(): " + str(e)

# function to see a movie is in orders
def checkInOrders(custId, movieId):
	try:
		query = "SELECT OrderId FROM Orders WHERE CustomerId = '%s' AND MovieId = '%s'" %(custId, movieId)
		args = (custId, movieId)
		cursor.execute(query)
		data = cursor.fetchall()
		
		if(len(data) > 0):
			return True
		else:
			return False
	except Exception as e:
		return "Error at checkInOrders(): " + str(e)
	
# function to see a movie is in orders
def checkCustomerInOrders(custId):
	try:
		query = "SELECT OrderId FROM Orders WHERE CustomerId = %s" %(custId)
		args = (custId)
		cursor.execute(query)
		data = cursor.fetchall()
		
		if(len(data) > 0):
			return True
		else:
			return False
	except Exception as e:
		return "Error at checkCustomerInOrders(): " + str(e)
	
def suggestions(customerID): #Suggestions
	try:
		#first, retrive customer's list of queued movies.
		listed = []
		movieID = []
		#the algorithm works the following way: 
		#BASELINE: Retrieve movies with similar tags.
		#ADDITIONAL OPTIONAL CONTRAINTS:     RETRIEVE MOVIES AND ORDER THEM ACCORDING TO AMOUNT OF RESEMBLANCE. That is, the more overlapping tags, the higher the suggestion.
		#execute query to obtain account number:
		query = "SELECT movieId FROM Orders where CustomerId like '%" + customerID + "%'"       #query function     
		cursor.execute(query)
		movieID = cursor.fetchone()
		#print(movieID[0])
		#movieID = movieID.translate(None, '(),\'')
		#print(movieID)

		query = "SELECT Genre FROM Movies WHERE id LIKE '%" + movieID[0] + "%'"       #query function

		#print(query)
		#CHEACK!

		result = []
		cursor.execute(query)
		result = cursor.fetchone()

	 # print(result[0])
		#CHECK!
		parsedResult = result[0].split('|')
		#print(parsedResult)


		for i in range(len(parsedResult)):
		# runs query to obtain ratings of movies with the specific genre.
				query = "SELECT Rating FROM Movies WHERE Genre LIKE '%" + parsedResult[i] + "%'"
				#print(query)
				cursor.execute(query)
				tmp = cursor.fetchall()
				#print(tmp)
			 #runs query to obtain all movieIDs
				query = "SELECT Id FROM Movies WHERE Genre LIKE '%" + parsedResult[i] + "%'"
				#print(query)
				cursor.execute(query)
				movieIDBuffer = cursor.fetchall()
				#print(movieIDBuffer)
				print("movieIDBuff datatype: " , type(movieIDBuffer[0]))

				#for j in range(len(tmp)):
				#    print(tmp[j])
				#    print(movieIDBuffer[j])
				#    print(str(tmp[j]).translate(None, '\'(),'))
				#    print(str(movieIDBuffer[j]).translate(None, '\'(),'))

				for j in range(len(tmp)):
						a = {'\'Id\':\''+ str(movieIDBuffer[j]).translate(None, '\'(),') + '\', \'Rating\':\'' + str(tmp[j]).translate(None, '(),') + '\', \'Poster\':\'../static/posters/' + str(movieIDBuffer[j]).translate(None, '(),') + '.jpg\''}
						b = {'Id': str(movieIDBuffer[j]).translate(None, '(),'), 'Rating': str(tmp[j]).translate(None, '\'(),'), 'Poster': '../static/posters/' + str(movieIDBuffer[j]).translate(None, '\'(),') + '.jpg'}
						#print(a)
						#print(b)
						listed.append(b)
		#listed = set(listed)
		#print(listed)
		return listed

	except Exception as e:
			return 'ERROR AT SUGGESTMOVIES(): ' + str(e)

# A function to get the list 
# -------------------------------------------------------------------
#												MAIN
# -------------------------------------------------------------------			
# App launches here
if __name__ == "__main__":
    app.run(debug=True)
		#http_server = WSGIServer(('', 5000), app)
		#http_server.serve_forever()