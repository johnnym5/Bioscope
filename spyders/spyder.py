from bs4 import BeautifulSoup
import csv
import urllib
import requests
import time
import MySQLdb
from random import randint

conn = MySQLdb.connect("localhost", "root", "root", "movieRental")
cursor = conn.cursor()

print "I'm an automated webcrawler, I'll sleep 1 second every iteration to avoid server timeout\n\n"

path = "/home/kittens/Downloads/movie_metadata.csv"
file = open(path, "r")
reader = csv.reader(file)


def getMovieId(title):
	return title[26:35]


def loadActors():
	actors = []
	movies = []

	for line in reader:
		actors.append(line[10])
		actors.append(line[6])
		actors.append(line[14])
		tmp = getMovieId(str(line[17]))
		movies.append(tmp)
		movies.append(tmp)
		movies.append(tmp)
		count += 1
		if (count == 59):
			break


	sortedActors = []
	sortedMovies = []
	starsIn = []

	hld = ""
	for actor in actors:
		if actor not in sortedActors:
			sortedActors.append(actor)
			sortedMovies.append('')

	for i in range(0, len(sortedActors)):
		for j in range(0, len(actors)):
			if ((sortedActors[i]) == (actors[j])):
				if sortedMovies[i] == '':
					sortedMovies[i] = (str(movies[j]))
				else:
					sortedMovies[i] = str(sortedMovies[i]) + '|' + str(movies[j])

	query = "INSERT INTO Actors(Name, Gender, Age, Movies, Rating) VALUES(%s, %s, %s, %s, %s)"

	for i in range (2, len(sortedActors)):
		args = (sortedActors[i], 'M', randint(18, 60), sortedMovies[i], randint(0,5))

		cursor.execute(query, args)
		data = cursor.fetchall()

		if len(data) is 0:
			conn.commit()
		else:
			print "Error"
	

def loadLinks():
	
	for line in reader:
		links.append(line[17])
		count += 1
		if(count == 60):
			break

def loadImages():
	links = []
	titles = []
	count = 0
	for line in reader:
		links.append(line[17])
		titles.append(getMovieId(str(line[17])))
		count += 1
		if(count == 60):
			break
		
	i = 0
	for link in links:
		if "http" in str(link):
			r = requests.get(link)
			
			desc = []
			data = r.text
			soup = BeautifulSoup(data, "lxml")

			posters = soup.find_all('img')
			
			for imgs in posters:
				if 'Poster' in str(imgs):
					src = imgs.get('src')
					urllib.urlretrieve(src, "static/posters/" + str(titles[i]) + ".jpg")

		i += 1
		time.sleep(1)		# Sleep to act human
			
			
def loadDescr():
	links = []
	count = 0
	for line in reader:
		links.append(line[17])
		count += 1
		if(count == 60):
			break
		
	thefile = open('descr.txt', 'w')
	
	for link in links:
		if "http" in str(link):
			r = requests.get(link)
			
			desc = []
			data = r.text
		
			descr = soup.find('div', {'class' : 'summary_text'})
			#desc.append(descr.text)
			thefile.write("%s\n" % descr.text.encode('utf-8'))
			time.sleep(1)		# Sleep to act human

def loadMovies():
	count = 0
	movieId = []
	direct = []
	dur = []
	actors = []
	genre = []
	title = []
	rating = []
	descr = []
	
	# load descriptions
	with open('descr.txt') as f:
		for line in f:
			descr.append(line.strip('\n'))
	
	print descr
		
	for line in reader:
		movieId.append(getMovieId(line[17]))
		direct.append(line[1])
		dur.append(line[3])
		actors.append(str(line[10]) + "|" + str(line[6]) + '|' + str(line[14]))
		genre.append(line[9])
		tmp = str(line[11])
		tmp = tmp[:len(tmp)-2] # remove unicode chars
		title.append(tmp)
		rating.append(line[25])		
		count += 1
		if (count == 59):
			break
	
	query = "INSERT INTO Movies(Id, Director, Duration, Actors, Genre, Title, Rating, Description) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
	
	for i in range(1, len(movieId)):
		args = (movieId[i], direct[i], dur[i], actors[i], genre[i], title[i], rating[i], descr[i-1])
		
		cursor.execute(query, args)
		data = cursor.fetchall()

		if len(data) is 0:
			conn.commit()
		else:
			print "Error"
	

loadMovies()
	
