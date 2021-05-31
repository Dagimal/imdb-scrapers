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
from core.bing_image_urls import bing_image_urls

parser = ConfigParser()
parser.read("config.conf")

imageStatus = parser.read('image-scraper','bing')

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
	try:
		num_loop = -1
		for i in movie_id:
			num_loop += 1
			if imageStatus == "on":
				configTemplate = open("core/index.html").read()
			else:
				configTemplate = open("core/index-no-images.html").read()
			prnt_loop = i.replace("\n","")

			title = scraper.get_title(prnt_loop)
			titles = title.display_title #PRINT TITLE ex.starWars
			if imageStatus == "on":
				images = ''.join(bing_image_urls(prnt_loop, limit=1))
			elif imageStatus == "off":
				pass
			#currency = title.budget_denomation #CURRENCY ex.USD
			budget = title.budget #BUDGET [INT]
			#totalBudget = currency+" "+str(budget) #BUDGET + CURRENCY
			country = title.country #PRINT COUNTRY
			language = title.language #PRINT LANGUAGE
			plot = title.plot #PRINT PLOT
			rating = title.mpaa_rating #PRINT RATING
			storyline = title.storyline #PRINT STORYLINE
			year = title.release_date #PRINT RELEASE DATE
			cast = title.top_cast
	#		topCast = [] #PRINT CAST
	#		for i in cast: #PRINT TO SINGLE LIST
	#			name = i.name_id
	#			credit = i.credit
	#			getName = scraper.get_name(name)
	#			act = getName.display_name + " as " + credit
	#			act.append(topCast)
			crew = scraper.get_full_crew(prnt_loop)
			fullCrew = [] #PRINT CREW
	#		for i in crew:
	#			name = i.name_id
	#			job = i.job_title
	#			getName = scraper.get_name(name)
	#			crewList = getName.display_name + " as "+job
	#			crewList.append(fullCrew)
			fullCrew = "antok kewer"
			topCast = "amanda"
			#EXPORT KE HTML
			if imageStatus == "on":
				changeText = {'language':language, 'country':country, 'rating':rating, 'images':images, 'title':titles, 'plot':plot, 'storyline':storyline, 'budget':budget, 'year':year, 'cast':topCast, 'crew':fullCrew}
			else:
				changeText = {'language':language, 'country':country, 'rating':rating, 'title':titles, 'plot':plot, 'storyline':storyline, 'budget':budget, 'year':year, 'cast':topCast, 'crew':fullCrew}
			t = Template(configTemplate, searchList=[changeText])
			configSave = open("output/html/"+str(num_loop)+"-"+titles.replace(" ","-")+".html","w")
			print(t, file=configSave)
		except:
			print("ada masalah, coba lagi")
def mainMenu():
	print("[1] EXPORT HTML")
	print("[2] EXPORT CSV")

banner()
mainMenu()

choice = input(">> ")

if choice == "1":
	exportHTML()
