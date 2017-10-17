# Project files for Movie Rental System - BioScope
![Bioscope](/static/img/logo_stroke2.png?raw=true "Optional Title")

This repository contains all the required files for the system. Make sure you do a pull request each time to make sure you have the updated contents of the system.

**PLEASE REFER to Manual.pdf for a full walkthrough and screenshots**

## Directory structure

* static 
	* Animations : Contains the background videos
	* img : Images/Favicons that are inlcuded in the website
	* js : JavaScipt files for AJAX queries
	* Stylesheets
	
* template
	* HTML files 
	
* spyders
	* Webscrapers for populating tables
	
## How to run

```
python app.py
```
## How to import the database
```
mysql -u username -p movieRental < db_dumps/movieRental.sql
```

## How to export the database
```
mysql -u username -p movieRental > db_dumps/movieRental.sql
```
