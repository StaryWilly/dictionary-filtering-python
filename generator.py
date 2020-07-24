print('Generator losowych hasel')
print('5 - 15 znakow , do pliku password.dat')

import string
import random
import secrets

liczba_hasel = 100
char_classes = (string.ascii_lowercase,
                    string.ascii_uppercase,
                    string.digits)
                    #string.punctuation)   # dodac aby byly znaki specjalne

size = lambda: secrets.choice(range(5,16))                  # Chooses a password.dat length.
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
    f = open(filename, mode)
    for i in range(1, 1001):
        password.append(pw())
        temp_pass = password[i - 1]
        # print("{0}. znakow: {1} : {2}".format(i,len(temp_pass),temp_pass))
        f.write(password[i - 1] + '\n')
    f.close()

a = clear_file("password4.dat")
b = generuj_plik("password4.dat", "a+")
print(a)
print(b)
