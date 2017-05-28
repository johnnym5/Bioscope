from flask import Flask, render_template, request, json, redirect, session
import MySQLdb
from werkzeug import generate_password_hash, check_password_hash
#from gevent.wsgi import WSGIServer


# ==========================================================

app = Flask(__name__)

# ========== MYSQL CONFIGURATION ==========================

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'movierRental'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = 'bolbbalgan4'
#mysql.init_app(app)

# ========== OPEN DATABASE CONNECTION =====================

conn = MySQLdb.connect("localhost", "root", "root", "movieRental")
cursor = conn.cursor()


# App route for main starting point
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
				return render_template('signIn_NewUser.html')
			else:
				return 'ERROR'

# App route to Sign Users in
@app.route("/SignIn")
def signIn():
	return render_template('signIn_NewUser.html')
			
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
		
		###
		#return str(data)
		
		if (len(data) > 0):
			if (_pwd == str(data[0][10])):
				session['user'] = data
				logged = True
				#return 'Logged In\n'
			#else:
				#return 'Wrong password\n'
		#else:
			#return 'Wrong email\n'

	except Exception as e:
		print e
		
	finally:
		return str(data)
		
			
# App launches here
if __name__ == "__main__":
    app.run(debug=True)
		#http_server = WSGIServer(('', 5000), app)
		#http_server.serve_forever()