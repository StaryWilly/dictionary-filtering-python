print('Generator losowych hasel')
print('5 - 15 znakow , do pliku password.dat')

import string
import random
import secrets
import time
from progress.bar import IncrementalBar

liczba_hasel = 100
char_classes = (string.ascii_lowercase,
                    string.ascii_uppercase,
                    string.digits)
                    #string.punctuation)   # dodac aby byly znaki specjalne

size = lambda: secrets.choice(range(3,20))                  # Chooses a password.dat length.
char = lambda: secrets.choice(secrets.choice(char_classes)) # Chooses one character, uniformly selected from each of the included character classes.
pw   = lambda: ''.join([char() for _ in range(size())])     # Generates the variable-length password.dat.

password = []

# czyszczenie pliku z haslami
def clear_file(filename):
    p = open(filename, "w+")
    p.write("")
    p.close()


# generator hasel
def generuj_plik(filename, mode):
    ilosc_hasel = 1001
    f = open(filename, mode)
    #bar = IncrementalBar('Generowanie', max=ilosc_hasel)
    for i in range(1, ilosc_hasel):
        #bar.next()
        password.append(pw())
        temp_pass = password[i - 1]

        # print("{0}. znakow: {1} : {2}".format(i,len(temp_pass),temp_pass))
        f.write(password[i - 1] + '\n')
    f.close()
file = "password2.dat"
a = clear_file(file)
b = generuj_plik(file, "a+")
print("Generije plik: {0}".format(file))



#print(a)
#print(b)
