from unittest.mock import patch
from unittest import TestCase

from DriexPlus1 import main


class Test3XPlus1(TestCase):
    @patch("builtins.input", return_value="3")
    def test_input_good(self, input):
        main()

    @patch("builtins.input", return_value="foo")
    def test_input_string(self, input):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    @patch("builtins.input", return_value="-1")
    def test_input_negatief(self, input):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)
