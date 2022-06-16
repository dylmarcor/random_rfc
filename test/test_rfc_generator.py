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

        # Test for txt type
        rand_num = str(random.randint(1, 9260))
        rfc = "https://www.rfc-editor.org/rfc/rfc" + rand_num
        form = 'txt'
        url = rfc_generator(rfc, form)
        self.assertEquals(url, "https://www.rfc-editor.org/rfc/rfc" + rand_num + "." + form)

if __name__ == "__main__":
    unittest.main()
