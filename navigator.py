from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import time
import random

class navigator:
    
    def __init__(self, username : str, password : str):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        
    def run(self):
        return
        
        
if __name__ == '__main__':
    navTest = navigator("username", "password")
    navTest.run()