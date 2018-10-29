import unittest
import requests


class TestyOfety(unittest.TestCase):

    def setUp(self):
        self.app = '' #tutaj trzeba odpalic flaska xd

    def test_pobierz_menu_restauracji(self):
        self.assertEqual(self.app, (50, 50),
                         'incorrect default size')
        r1 = requests.get("http://127.0.0.1:5000/pobierz_menu_restauracji", params={'id_restauracji': 0})
        print(r1.text)

        if r1.text == '[[1,"Ciastko",29.99,"Pycha ciacho"],[2,"Kawa",5.99,"Dobra kawusia"]]':
            print("SUCCESS!")
        else:
            print("FAILURE!")


