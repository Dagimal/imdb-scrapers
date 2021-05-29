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
from core.Cheetah.Template import Template
from configparser import ConfigParser

parser = ConfigParser()
parser.read("config.conf")

def banner():
	print(
		"""
   ______  ______  ___  ____                         
  /  _/  |/  / _ \/ _ )/ __/__________ ____  ___ ____
 _/ // /|_/ / // / _  |\ \/ __/ __/ _ `/ _ \/ -_) __/
/___/_/  /_/____/____/___/\__/_/  \_,_/ .__/\__/_/   
                                     /_/             
""")

def exportCSV():

def exportHTML():

def mainMenu():
	print("[1] EXPORT CSV")
	print("[2] EXPORT HTML")
input(">> ")
banner()
