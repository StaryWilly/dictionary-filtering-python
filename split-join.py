from pathlib import Path



input_file = "password.dat"
def file_len(input):
    with open(input) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



def split_file(input,  pozycja_start, pozycja_stop):
    #source_file = open(input, "r")

    numer_pliku = 1
    with open(input) as f:
        for i, l in enumerate(input):
            output = input + ".{0}.split".format(numer_pliku)
            dest_file = open(output, "w+")

            if i >= pozycja_start and i < pozycja_stop:
                print("Pozycja start{0}".format(pozycja_start))
                print("Pozycja stop{0}".format(pozycja_stop))
                dest_file.write(l)
                print("Linia nr: {0}".format(i))
            elif i == pozycja_stop:
                print("Koniec pliku na linii: {0}".format(i))
                numer_pliku += 1
                pozycja_start += wynik_koncwy
                pozycja_stop += wynik_koncwy

    return i + 1

a = file_len(input_file)
print(a)
wielkosc = Path(input_file).stat().st_size
#podzial_linii = 5 * 1000000 # w MB
podzial_linii = 5 * 10 # w MB
wynik = a * podzial_linii
wynik_koncwy = wynik / wielkosc
print(wynik_koncwy)
print("W zaokragleniu: {0}".format(round(wynik_koncwy)))

pozycja_start = 1
pozycja_stop = wynik_koncwy

b = split_file("password.dat", pozycja_start, pozycja_stop)
print(b)



