"""
RFC Unit Test's
"""

import unittest
import random
from src import random_rfc

rfc_generator = random_rfc.rfc_generator

class TestRfc(unittest.TestCase):

    def test_rfc_generator(self):
        """
        Test that a correct URL is generated
        """
        rand_num = str(random.randint(1, 9260))
        RFC_EDITOR_URL = "https://www.rfc-editor.org/rfc/rfc"
        rfc = RFC_EDITOR_URL + rand_num

        # Test for txt type
        form = 'txt'
        url = rfc_generator(rfc, form)
        self.assertEqual(url, RFC_EDITOR_URL + rand_num + "." + form)
        # Test for html type
        form = 'html'
        url = rfc_generator(rfc, form)
        self.assertEqual(url, RFC_EDITOR_URL + rand_num + "." + form)


if __name__ == "__main__":
    unittest.main()
