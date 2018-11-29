# coding=utf-8
lista_pracownikow = {
    'list_pracownikow': [
        {
            'id_pracownika': 'janPan',
            'id_restauracji': 1,
            'imie': 'Jan',
            'nazwisko': 'Nowak',
            'telefon': '123456789',
            'stanowisko': 'pracownik kuchni',
            'haslo': 'soicrupogi'
        },
        {
            'id_pracownika': 'AAmen',
            'id_restauracji': 2,
            'imie': 'Andrzej',
            'nazwisko': 'Adrianowski',
            'telefon': '777888999',
            'stanowisko': 'dostawca',
            'haslo': '39084utco'

        },
        {
            'id_pracownika': 'KNow',
            'id_restauracji': 4,
            'imie': 'Kasia',
            'nazwisko': 'Nowak',
            'telefon': '333444555',
            'stanowisko': 'menadzer restauracji',
            'haslo': 'kKdPS'

        }
    ]
}

print(lista_pracownikow)

k = 0
for pracownik in lista_pracownikow['list_pracownikow']:
    if pracownik['id_pracownika'] == 'AAmen':
        lista_pracownikow['list_pracownikow'].pop(k)
    k += 1

print(lista_pracownikow)