from pathlib import Path



input_file = "password.dat"
def file_len(input):
    with open(input) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



def split_file(input,  pozycja_start, pozycja_stop):
    source_file = open(input, "r")

    numer_pliku = 1
    for i, l in enumerate(source_file):
        output = input + ".{0}.split".format(numer_pliku)
        dest_file = open(output, "a+")
        #print("docelowy plik: {0}".format(output))
        if i >= pozycja_start and i < pozycja_stop:
            print("Aktualne haslo: {0}".format(l))
            #print("Pozycja start: {0}".format(pozycja_start))
            #print("Pozycja stop: {0}".format(pozycja_stop))
            dest_file.write(l)
            #print("Linia nr: {0}".format(i))
        elif i == pozycja_stop:
            print("Koniec pliku na linii: {0}".format(i))
            numer_pliku += 1
            pozycja_start += round(wynik_koncwy)
            pozycja_stop += round(wynik_koncwy)
            #print("Wynik koncowy: {0}".format(wynik_koncwy))
            #print("Pozycja start nowy plik: {0}".format(pozycja_start))
            #print("Pozycja stop nowy plik: {0}".format(pozycja_stop))



a = file_len(input_file)
print("Wielkosc pliku Input: {0}".format(a))
wielkosc = Path(input_file).stat().st_size
#podzial_linii = 5 * 1000000 # w MB
podzial_linii = 5 * 10 # w MB
print("Podzial linii: {0}".format(podzial_linii))
wynik = a * podzial_linii
wynik_koncwy = wynik / wielkosc
#print("Wynik koncowy: {0}".format(wynik_koncwy))
#print("W zaokragleniu: {0}".format(round(wynik_koncwy)))

pozycja_start = 1
pozycja_stop = round(wynik_koncwy)

b = split_file("password.dat", pozycja_start, pozycja_stop)
print(b)



