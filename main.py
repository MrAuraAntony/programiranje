def ucitaj_tekst(filepath):
    try:
    #ovdje ide logika za čitanje datoteke
        with open (filepath,'r',encoding='uth-8') as file:
         sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f'greška: Datoteka na putanji {filepath} ne postoji.')
        return None #vraća prazan skup podataka, ako ne nađe datoteku


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