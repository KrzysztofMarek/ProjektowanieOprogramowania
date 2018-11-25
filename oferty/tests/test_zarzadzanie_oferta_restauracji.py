import unittest

import oferty.zarzadzanie_oferta_restauracji as zo_restauracji

from oferty.Constants import Constants

class TestZarzadzanieOferta(unittest.TestCase):

    def test_waliduj_danie(self):
        waliduj_danie = zo_restauracji.waliduj_danie
        poprawne_danie = {Constants.Danie_data.NAZWA: "Dobre danie",
                          Constants.Danie_data.CENA: "100,12",
                          Constants.Danie_data.OPIS: "Prawdziwie dobre danie."}
        danie_bez_danych = {Constants.Danie_data.NAZWA: "Dobre danie!"}
        danie_niepoprawne_dane = {Constants.Danie_data.NAZWA: "zla_nazwa! ###",
                                  Constants.Danie_data.CENA: "120312.1",
                                  Constants.Danie_data.OPIS: "Najgorszy_opis%#"}

        self.assertTrue(waliduj_danie(poprawne_danie))
        self.assertFalse(waliduj_danie(danie_bez_danych))
        self.assertFalse(waliduj_danie(danie_niepoprawne_dane))

    def test_waliduj_nazwe(self):
        waliduj_nazwe = zo_restauracji.waliduj_nazwe
        nazwa_poprawna = "Poprawna nazwa\t"
        nazwa_brak_uppercase = "zla nazwa"
        nazwa_zle_znaki = "Zla %nazwa3"

        self.assertFalse(waliduj_nazwe(nazwa_zle_znaki))
        self.assertFalse(waliduj_nazwe(nazwa_brak_uppercase))
        self.assertTrue(waliduj_nazwe(nazwa_poprawna))

    def test_waliduj_cene(self):
        waliduj_cene = zo_restauracji.waliduj_cene
        cena_poprawna = "100,12"
        cena_poprawna_krotka = "100,1"
        cena_bez_przecinka = "100.1"

        self.assertTrue(waliduj_cene(cena_poprawna))
        self.assertTrue(waliduj_cene(cena_poprawna_krotka))
        self.assertFalse(waliduj_cene(cena_bez_przecinka))

    def test_waliduj_opis(self):
        waliduj_opis = zo_restauracji.waliduj_opis()
        opis = "abcde"
        opis_niepoprawny = "!@#askaoisdnofsd"

        self.assertTrue(waliduj_opis(opis))
        self.assertFalse(waliduj_opis(opis_niepoprawny))

