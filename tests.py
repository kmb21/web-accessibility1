import Unittest
import argparse as argp
from accessibilitySoup import Soup
from replaceHelper import *

class testAccesibilitySoup(Unittest.TestCase):
    def setUp(self):
        parser = argp.ArgumentParser(description="Accessibility soup program \
for document scraping")
        parser.add_argument("file_name", help = "Path to soup file")
        args = parser.parse_args()
        self.soup_file = Soup(args.file_name)
        
    def testHtmlTag(self):
        """
        Check if the lang attribute in the html 
            tag is correctly identified
        """
        htmlTag(Soup)
        
        