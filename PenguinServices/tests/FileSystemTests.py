from FileSystem import Find
import unittest

class TestFind(unittest.TestCase):
    def setUp(self):
        flatFiles = Find("/home/fox/Desktop/LoggerFrogger/", [r'.*', r'.*[.]py'])
        self.foundFiles = flatFiles()
    
    # Test/OS Specific
    def test_count(self):
        self.assertEqual(len(self.foundFiles), 7, "Length should be 7")
    
    # Test/OS Specific
    def test_last(self):
        self.assertEqual(self.foundFiles[-1], '/home/fox/Desktop/LoggerFrogger/LoggerFrogger/cronManager.py', "Final file should be cronManager.py") 
