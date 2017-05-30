from bs4 import BeautifulSoup
import csv
import urllib
import requests
import time

print "I'm an automated webcrawler, I'll sleep 1 second every iteration to avoid server timeout"

path = "/home/kittens/Downloads/movie_metadata.csv"
file = open(path, "r")
reader = csv.reader(file)

links = []
count = 0;

for line in reader:
	links.append(line[17])
	count += 1
	if(count == 60):
		break
	
for link in links:
	if "http" in str(link):
		r = requests.get(link)
	
		data = r.text
		soup = BeautifulSoup(data, "lxml")

		#posters = soup.find_all('img')
		#for imgs in posters:
		#	if 'Poster' in str(imgs):
		#		src = imgs.get('src')
		#		name = imgs.get('alt')			
		#		#urllib.urlretrieve(src, "posters/" + name + ".jpg")
				
		descr = soup.find('div', {'class' : 'summary_text'})
		print descr.text
		time.sleep(1)		# Sleep to act human


