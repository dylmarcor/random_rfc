"""
RFC Unit Test's
"""

import unittest
import ..src.random_rfc.py

class TestRfc(unittest.TestCase):

    def test_rfc_generator(self):
        """
        Test that a correct URL is generated
        """

        # Test for txt type
        http = "https://www.rfc-editor.org/rfc/rfc"
        rand_num = 3452
        form = 'txt'
        url = rfc_generator(http, 3452, form)
        self.assertIs(url, "https://www.rfc-editor.org/rfc/rfc3452.txt")

if __name__ = "__main__":
    unittest.main()
