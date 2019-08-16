import sys, os, unittest
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.utils import ConnectionCache
from AWSLibrary.keywords import SessionKeywords
from AWSLibrary.base import LibraryComponent
from unittest.mock import Mock


class SessionKeywordsTests(unittest.TestCase): 

    def setUp(self):
        self.lib = Mock(AWSLibrary)
        self.session_keywords = SessionKeywords(self.state)
        self.region = "us-east-1"

    def test_class_should_initiate(self):
        """Class init should instantiate required classes."""
        self.assertIsInstance(self.session_keywords._builtin, BuiltIn)
        self.assertIsInstance(self.session_keywords._cache, ConnectionCache)