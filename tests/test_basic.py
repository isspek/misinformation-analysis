# -*- coding: utf-8 -*-

from .context import app
from app.utils import parse_url
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_url_parser(self):
        url = 'http://www.bbc.com/news/world-us-canada-41419190'
        self.assertEqual('bbc.com',parse_url(url))



if __name__ == '__main__':
    unittest.main()