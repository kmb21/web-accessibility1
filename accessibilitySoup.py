from bs4 import BeautifulSoup
from replaceHelper import *

##In future implementation, include adaptive editing features like making lists, etc
class Soup():
    def __init__(self, filepath):
        self.path = filepath
        self.soup = None
        self.sup_dict = {} #Used for superscripts
        self.fnote_dict = {}
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
        superScriptTag(self.soup, self.fnote_dict)
        replaceEllipsis(self.soup)
        replaceSemicolon(self.soup)
        replaceCopySymbol(self.soup)
        tableTags(self.soup)
        accents(self.soup)
        mdash(self.soup)
        
        #print(self.soup)
        
        
        
    def savefile(self, path):
        """
        Given a path to save the file at, the function writes the updated code
        to a new file
        Args:
            path (string): Path to store updated code
        """
        saveFile(self.soup, path)
        
    # def standard_remove(self):
    #     """
    #     unwraps standard things like <span class font = 0 ... and others
    #     """
                
    # def __str__(self):
    #     """
    #     This enables users to see the current version of the file they are trying
    #     to edit
    #     Returns:
    #         A string of the file showing the current progress of how the file currently
    #         looks like. GUI will handle this
    #     """
    #     return "%s"%self.soup.prettify()
    
    # def filter_tags(self, tag):
    #     pass
    
    # def replace_tag(self, tag):
    #     pass
    
    # def replace_section(self):
    #     pass

if __name__ == "__main__":
    # test1 = Soup("/Users/maxwellkumbong/Desktop/web-accessibility1/Goldstein.html")
    # test1.standardized()
    print("In main")
    



        
        