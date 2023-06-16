from bs4 import BeautifulSoup
import tkinter as tk
import re
from replaceHelper import *

##Uses GUI, to be implemented later

##In future implementation, include adaptive editing features like making lists, etc
class Soup():
    def __init__(self, filepath):
        self.path = filepath
        self.soup = None
        self.fnote_dict = {} #Used for superscripts
        while self.soup is None:
            try:
                self.file = open(self.path, "r")
                self.soup = BeautifulSoup(self.file, "html.parser")
            except:
                self.soup = None
                self.path = input("Please enter a valid path: ")
            ##Need to handle exception in main
        
    def removetag(self, tagName):
        """
        This method removes all tags in the file by finding all of them
        and removing them
        Args:
            tagName (string): The name of the tag e.g "div", "b"
            Note: Do not include < or > as a parameter, just the name
        """
        for tag in tagName:
            tag = tag.strip()
            tagsFound = self.soup.find_all(tagName)
            for tag in tagsFound:
                tag.unwrap()
                
    def standardized(self):
        """
        Replaces standard things which each file always has
        for example the information enclosed by <head>, &nsbp, bold, italic, ""
        """
        htmlTag(self.soup)
        headTag(self.soup)
        strongTag(self.soup)
        italicTag(self.soup)
        standardSpan(self.soup)
        spacingNSBP(self.soup)
        divTag(self.soup)
        quotTags(self.soup)      
        imgTag(self.soup)
        brTags(self.soup)
        bookmarks(self.soup)
        print(self.soup)
        saveFile(self.soup)
        
    def standard_remove(self):
        """
        unwraps standard things like <span class font = 0 ... and others
        """
                
    def __str__(self):
        """
        This enables users to see the current version of the file they are trying
        to edit
        Returns:
            A string of the file showing the current progress of how the file currently
            looks like. GUI will handle this
        """
        return "%s"%self.soup.prettify()
    
    def filter_tags(self, tag):
        pass
    
    def replace_tag(self, tag):
        pass
    
    def replace_section(self):
        pass

###TODO: Make standard changes to files, ie there are standard things which all files
#so automatically implement these before user starts changing things.

##In gui, there should be a wayh to see current state of text

if __name__ == "__main__":
    test1 = Soup("/Users/maxwellkumbong/Desktop/web-accessibility1/Goldstein.html")
    #tags = input("Enter the tags you want to remove separated by commas: ")
    #tagList = tags.split(",")

    #test1.removetag(tagList)
    #print(test1)
    test1.standardized()
    
    #print(test1)


        
        