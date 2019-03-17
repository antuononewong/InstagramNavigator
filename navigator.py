from selenium import webdriver
from urllib.parse import urlparse
import time

#Simple crawler that explores a specific hashtags pictures. 
#It uses selenium to handle http requests and parse the HTML/CSS of Instagram. 

class navigator:
    
    def __init__(self, hashtag : str, loops : int):
        self.hashtag = hashtag
        self.loops = loops
        self.driver = webdriver.Firefox()
    
    #Navigate to the page using the inputed hashtag.
    def openPageAtHashtag(self):
        return
    
    #Grabs and parses the pictures considered in view on the browser
    def getPictures(self):
        return
    
    #Clicks on each picture and shows the comments/likes/etc... then closes it and moves on to the next picture.
    def openPictures(self, picLinks_hrefs : list):
        return
    
    #Grabs and opens pictures for loops number of times        
    def openPicturesAtHashtag(self):
        return
        
    #Closes open web browser and stops the program
    def stop(self):
        self.driver.close()
    
    #Opens web browser, navigates to specific hashtag, then begins opening pictures      
    def run(self):
        self.openPageAtHashtag()
        self.openPicturesAtHashtag()
        
        
if __name__ == '__main__':
    navTest = navigator("samoyed", 3)
    navTest.run()