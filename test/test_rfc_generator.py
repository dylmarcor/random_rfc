"""
RFC Unit Test's
"""

import unittest
from ..src.random_rfc.py import *

class TestRfc(unittest.TestCase):

    def test_rfc_generator(self):
        """
        Test that a correct URL is generated
        """

        # Test for txt type
        rfc = "https://www.rfc-editor.org/rfc/rfc"
        rand_num = 3452
        form = 'txt'
        url = rfc_generator(rfc, form)
        self.assertIs(url, "https://www.rfc-editor.org/rfc/rfc3452.txt")

if __name__ == "__main__":
    unittest.main()
