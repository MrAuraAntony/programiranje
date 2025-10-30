"""
moja_lista = []
moja_lista.append(10)
moja_lista.append(20)
moja_lista.append(30)

print(moja_lista)

print(moja_lista[1])

print(moja_lista[0:2])

moja_lista.remove(20)

print(moja_lista)
"""
"""
voće = ["jabuka", "banana", "kruška"]
print(voće[0])
voće.append("naranča")
print(voće)
"""
"""
# Ovo je 2D lista (3 retka, 3 stupca)
ormar = [
    ['majica', 'kapa', 'sal'],    # 0. redak (polica)
    ['hlace', 'carape', 'remen'], # 1. redak
    ['jakna', 'cipele', 'cizme']  # 2. redak
]
print(ormar[1])

print(ormar[1][1])
"""
"""
# Ovo je 2D lista (3 retka, 3 stupca)
ormar = [
    ['majica', 'kapa', 'sal'],    # 0. redak (polica)
    ['hlace', 'carape', 'remen'], # 1. redak
    ['jakna', 'cipele', 'cizme']  # 2. redak
]

for redak in ormar:
    print(redak[1])
"""
"""

def pronadji_broj (lista, trazeni_broj):
    for broj in lista:
        if broj == trazeni_broj:
            provjera =True
            break
        else:
            provjera = False
    if provjera:
        print (f"Broj {trazeni_broj} je na listi")
    else:
        (f"Broj {trazeni_broj} nije na listi")


provjera = False

lista_brojeva = [10, 20, 30, 40, 50]
trazeni_broj = 30

pronadji_broj(lista_brojeva, trazeni_broj)
"""
tablica = [['Riječ', 'Frekvencija']]

rezultati = [('hlapić', 15), ('gita', 12), ('majstor', 10)]

for rezultati in tablica