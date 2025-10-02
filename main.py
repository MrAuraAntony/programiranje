STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'bi', 'bio', 'bila', 'što', 'ga', 'su', 'joj', 'ih']
def ucitaj_tekst(filepath):
    try:
    #ovdje ide logika za čitanje datoteke
        with open (filepath,'r',encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f'greška: Datoteka na putanji {filepath} ne postoji.')
        return None #vraća prazan skup podataka, ako ne nađe datoteku

#funkcija koja pročišćava tekst

def ocisti_tekst(tekst):
    #ovdje ide logika za pročišćavanje teksta
    tekst = tekst.lower()
    interpunkcija = ['.', ',', ':', ';', '?', '!', '"', "'", '(', ')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_riječi = tekst.split()

    return lista_riječi

#koliko se puta ponavlja ista riječ
def broji_frekvenciju(lista_rijeci):
    # Kreiramo prazan skup di skupljamo rezultate
    rjecnik_frekvencija = {}

    # Prolazimo kroz sbvaku riječ u primljenoj listi
    for rijec in lista_rijeci:
        if rijec in rjecnik_frekvencija:
            rjecnik_frekvencija[rijec] += 1
        else:
            rjecnik_frekvencija[rijec] = 1
    return rjecnik_frekvencija


#glavni dio programa
if __name__ == '__main__':
    filepath = 'tekst.txt'
    print(f'učitavam tekst iz datoteke :{filepath}')

    ucitani_tekst = ucitaj_tekst(filepath)

    if ucitani_tekst:
        print('\ntekst uspješno učitan. slijedi ispis sadržaja:')
        print('-' * 40)
        print(ucitani_tekst)
        print('-' * 40)
    else:
        print('program se prekida jer tekst nije učitan.')

    procisceni_tekst = ocisti_tekst(ucitani_tekst)

    if procisceni_tekst:
        print("\nProcisceni tekst je: ")
        print('-' * 40)
        print(procisceni_tekst)
        print('-' * 40)
        print(procisceni_tekst.__len__())
    else:
        print("program se prekida jer tekst nije pročitan")
        
    if procisceni_tekst:
        print("\nProcisceni tekst je")
        print('-' * 40)
        print(procisceni_tekst)
        print('-' * 40)
        #Brojimo riječi za frekvencije
        print("Brojim frekvenciju riječi...")
        broj_rijeci = broji_frekvenciju(procisceni_tekst)
        print("Brojanje završeno!")

        #Ispisujemo rezultat da vidimo što smo dobili
        print("\n---Rjecnik frekvencije---")
        print(broj_rijeci)
        print("-" * 40)
    else:
        print('Program se prekida jer tekst nije pročitan')
