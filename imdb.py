"""
+++ IMDB Scraper +++
Author  :: Dagimal Autobots
E-Mail  :: daffagifariakmal@gmail.com
Date    :: 30-May-2021
Version :: 0.1
================================
thanks to [Allah SWT]
thanks to [zembrodt] for this cool library 😎
"""
import core.pymdb
from core.Cheetah.Template import Template
from configparser import ConfigParser

parser = ConfigParser()
parser.read("config.conf")

# baca file id
movie_id = open("movie_id.txt","r").readlines()

# scraper
scraper = core.pymdb.PyMDbScraper(rate_limit=500)

def banner():
	print(
		"""
   ______  ______  ___  ____                         
  /  _/  |/  / _ \/ _ )/ __/__________ ____  ___ ____
 _/ // /|_/ / // / _  |\ \/ __/ __/ _ `/ _ \/ -_) __/
/___/_/  /_/____/____/___/\__/_/  \_,_/ .__/\__/_/   
                                     /_/             
""")
	
#def exportCSV():
#
def exportHTML():
	num_loop = -1
	for i in movie_id:
		num_loop += 1
		configTemplate = open("core/index.html").read()
		prnt_loop = i.replace("\n","")

		title = scraper.get_title(prnt_loop)
		titles = title.display_title #PRINT TITLE ex.starWars
		currency = title.budget_denomation #CURRENCY ex.USD
		budget = title.budget #BUDGET [INT]
		totalBudget = currency+" "+str(budget) #BUDGET + CURRENCY
		country = title.country #PRINT COUNTRY
		language = title.language #PRINT LANGUAGE
		plot = title.plot #PRINT PLOT
		rating = title.mpaa_rating #PRINT RATING
		storyline = title.storyline #PRINT STORYLINE
		year = title.release_date #PRINT RELEASE DATE
		cast = title.top_cast #PRINT CAST

		#EXPORT KE HTML
		changeText = {'title':title, 'plot':plot, 'storyline':storyline, 'director':director, 'writer':writer, 'budget':budget, 'year':year, 'cast':cast}
		t = Template(configTemplate, searchList=[changeText])
		configSave = open("output/html/"+num_loop+"-"+titles.replace(" ","-")+".html","w")
		print(t, file=configSave)
def mainMenu():
	print("[1] EXPORT HTML")
	print("[2] EXPORT CSV")

banner()
mainMenu()

choice = input(">> ")

if choice == "1":
	exportHTML()
