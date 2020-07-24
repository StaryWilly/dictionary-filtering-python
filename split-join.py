from pathlib import Path


input_file = "password.dat"
def file_len(input):
    with open(input) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
a = file_len(input_file)
print(a)
wielkosc = Path(input_file).stat().st_size
podzial_linii = 5000000 # w MB
wynik = a * podzial_linii
wynik_koncwy = wynik / wielkosc
print(wynik_koncwy)
print("W zaokragleniu: {0}".format(round(wynik_koncwy)))


pozycja_start = 1
pozycja_stop = wynik_koncwy
pozycja_start += wynik_koncwy
pozycja_stop += wynik_koncwy

# def min_max_pw(min, max, input, output):
#     source_file = open(input, "r")
#     dest_file = open(output, "w")
#     for line in source_file:
#         if len(line) > min and len(line) < max:
#             dest_file.write(line)

