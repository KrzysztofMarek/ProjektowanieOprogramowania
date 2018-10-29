import unittest
from zaslepki_baz_danych import oferty, realizacja, zamowienia, zarzadzanie_personelem


class TestyOfety(unittest.TestCase):
    def setUp(self):
        self.app = oferty.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
        pass

    def test_pobierz_menu_restauracji(self):
        #r1 = self.app.get('/pobierz_menu_restauracji', json={'id_restauracji': 0})
        r1 = self.app.get('/pobierz_menu_restauracji', query_string=dict(id_restauracji=0))
        print(r1.data)
        print("JSON:")
        print(r1.get_json())
        #assert '[[1,"Ciastko",29.99,"Pycha ciacho"],[2,"Kawa",5.99,"Dobra kawusia"]]' in r1


class TestyRealizacja(unittest.TestCase):
    def setUp(self):
        self.app = realizacja.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
         #wyłaczenie flaska
        pass

  #  def test_pobierz_menu_restauracji(self):
        #r1 = self.app.get('/pobierz_menu_restauracji', json={'id_restauracji': 0})
        #data = {'id_restauracji': 0}
        #r1 = self.app.get('/pobierz_menu_restauracji', query_string=dict(id_restauracji=0))
        #print(r1.data)
        #print("JSON:")
        #print(r1.get_json())
        #assert '[[1,"Ciastko",29.99,"Pycha ciacho"],[2,"Kawa",5.99,"Dobra kawusia"]]' in r1


if __name__ == '__main__':
    unittest.main()
