from bs4 import BeautifulSoup
import re

##Uses GUI, to be implemented later

##In future implementation, include adaptive editing features like making lists, etc
class Soup():
    def __init__(self, filepath):
        self.path = filepath
        try:
            self.file = open(self.path, "r")
            self.soup = BeautifulSoup(self.file, "html.parser")
        except:
            self.soup = None
            raise Exception("File path is invalid")
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
                
    def standard_replace(self):
        """
        Replaces standard things which each file always has
        for example the information enclosed by <head>, &nsbp, bold, italic, ""
        """
        
        html = self.soup.find("html")
        new_tag = self.soup.new_tag("html")
        html.replace_with(new_tag)
        new_tag["lang"] = "en"
        
        tag = self.soup.find("html")
        previous = tag.find_all_previous()
        html_tag = self.soup.find('html')  # Find the <html> tag

# Remove all elements preceding the <html> tag
        previous_elements = html_tag.find_previous_siblings()
        for element in previous_elements:
            element.extract()
        new_tag.insert_before(("<!Doctype HTML>"))
        print(self.soup)
        
        #<!DOCTYPE HTML>
        #<html lang="en">
        found = self.soup.find("html")
        #Replaces context of head tag with standard template
        found.string = """
<head>
<title>Chapter Number Chapter title | Book Title</title>
<meta charset="utf-8">
<style>
body {
    font-size: 16px;
    font-family: Verdana, "sans-serif";
} p {
    line-height: 1.5em;
} ul {
    list-style-type:none;
} .bib {
text-indent:-2em;
margin-left:0em;
line-height: 1.5em;
    }
</style>
</head>"""
    
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
    test1 = Soup("/Users/maxwellkumbong/Desktop/web-accessibility1/tesstFile.html")
    #tags = input("Enter the tags you want to remove separated by commas: ")
    #tagList = tags.split(",")

    #test1.removetag(tagList)
    #print(test1)
    test1.standard_replace()
   #print(test1)

        
        