import pymongo
from menu import Menu
from database import Database
from models.blog import Blog
Database.initialize()
menu = Menu()
menu.run_menu()
