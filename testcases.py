import unittest

from accessibilitySoup import Soup

class TestSoup(unittest.TestCase):
    
    def setUp(self): #Creates a soup object
        self.soup = Soup() #think of a way to not use a filepath but still use the constructor
        
        
    def test_head_Tag(self):
        