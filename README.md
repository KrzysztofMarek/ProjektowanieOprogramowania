# ProjektowanieOprogramowania

Nasz projekt na studia - wrzucamy kod do swoich branchy ;)


HOW TO RUN!!!!:

-java i gradle:
1. Wchodzimy do folderu.
2. gradlew build
3. gradlew run

-angular:
1. Wchodzimy do folderu.
2. npm install
3. ng serve --port="wolny numer portu"


PORTY:

    zarzadzanie_personelem = 9090
    baza_personel = 9091
    platnosci = 9092
    bank = 9093
    zarzadzanie_siecia = 9094
    baza_zarzadzanie_siecia = 9095

    platnosci_gui = 4200
    ui_menadzera_sieci = 4201
    ui_menadzera_restauracji = 4202

PROBLEMY Z DEPLOYMENTEM:

- gradle nie znajduje czegoś .jar
1. Dodaj zmienną środowiskową JAVA_HOME, która wskazuje ścieżkę do Twojego jdk.
2. Rozszerz zmienną PATH o treść "%JAVA_HOME%\bin;" (dla Windowsa)
