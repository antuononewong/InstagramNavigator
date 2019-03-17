from selenium import webdriver
from urllib.parse import urlparse
import time

# Simple crawler that explores a specific hashtags pictures. 
# It uses selenium to handle http requests and parse the HTML/CSS of Instagram. 

class navigator:
    
    def __init__(self, hashtag : str, loops : int):
        self.hashtag = hashtag
        self.loops = loops
        self.driver = webdriver.Firefox()
    
    # Navigate to the page using the inputed hashtag
    def openPageAtHashtag(self):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + self.hashtag + "/?hl=en") # Navigate to page @ specific hashtag
        time.sleep(4) # Allow page to load
    
    # Grabs and parses the pictures considered in view on the browser
    def getPictures(self):
        driver = self.driver
        
        # Experiment with range here to see differences in repeated grabbing of the same picture.
        # The top 9 posts will always be grabbed no matter how far page is scrolled.
        # This case is ignored when parsing to keep memory usage low if an "already-searched" list is stored.
        for _ in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) # As you scroll more and more it takes time to load in the incoming pictures
            
        # Searching for picture links then parsing out ones not needed like the explore page
        hrefs = driver.find_elements_by_tag_name('a')
        picLinks_hrefs = [ref.get_attribute('href') for ref in hrefs]
        picLinks_hrefs = [urlparse(href).path for href in picLinks_hrefs if "https://www.instagram.com/p/" in href]
        
        return picLinks_hrefs
    
    # Clicks on each picture and shows the comments/likes/etc... then closes it and moves on to the next picture
    def openPictures(self, picLinks_hrefs : list):
        driver = self.driver
        if len(picLinks_hrefs) == 0:
            print("No pictures were found. Check internet connection or getPictures() function.")
            return
        
        for picLink in picLinks_hrefs:
            try:
                picBox = driver.find_element_by_xpath("//a[@href='" + picLink + "']")
                driver.execute_script("arguments[0].click();", picBox)
                time.sleep(4) # Allow picture to open
                driver.find_element_by_class_name("ckWGn").click() # Finds close button in HTML and exits out of picture view
                time.sleep(1) # Gives picture time to close
            except:
                print("Failed to open or close the photo at " + picLink)
                continue # Fail on a specific picture we move on to the next
    
    # Grabs and opens pictures for loops number of times        
    def openPicturesAtHashtag(self):
        picLinks_hrefs = self.getPictures()
        self.openPictures(picLinks_hrefs)
        
    # Closes open web browser and stops the program
    def stop(self):
        self.driver.close()
    
    # Opens web browser, navigates to specific hashtag, then begins opening pictures.
    # Cleanly closes browser after finding/opening all pictures in search parameters.
    def run(self):
        self.openPageAtHashtag()
        self.openPicturesAtHashtag()
        self.stop()
        
        
if __name__ == '__main__':
    navTest = navigator("samoyed", 3)
    navTest.run()