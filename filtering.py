
# Iterating over each line in the file using for in loop

# with open("password.dat") as file_handle:
#     for line in file_handle.readlines():
#         print(line, end='')

import glob, os
import logging
import threading
import time

min_pass = 5
max_pass = 15

def search_dat_files(path):
    source_file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("dat"):
                #print(os.path.join(root, file))
                source_file_list.append(file)
    return source_file_list

pliki = search_dat_files("/home/willy/PycharmProjects/dictionary-filtering-python/")
#print(pliki)
#print(pliki[0])



def min_max_pw(min, max, input, output):
    source_file = open(input, "r")
    dest_file = open(output, "w")
    for line in source_file:
        if len(line) > min and len(line) < max:
            dest_file.write(line)


#min_max_pw(5,15,"password.dat","password2.dat")

def duplicate_pw(input, output):
    with open(input) as result:
        uniqlines = set(result.readlines())
        with open(output, 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

#duplicate_pw("password2.dat","password3.dat")

# czyszczenie plików
def clear_file(filename):
    p = open(filename, "w+")
    p.write("")
    p.close()


def filtrowanie_plikow(min, max, input):
    temp_file = input
    temp_file += ".tmp"
    output = input + ".filtered"
    min_max_pw(min,max,input,temp_file)
    duplicate_pw(temp_file,output)
    #clear_file(temp_file)
    os.remove(temp_file)



# test filtrowania:
# source_file = open("password.dat", "r")
# print("Source:")
# print(source_file.read())
# print()
# print("Dest:")
# dest_file = open("password3.dat", "r")
# print(dest_file.read())
# dest_file.close()

def thread_function(name, plik):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    result = filtrowanie_plikow(min_pass, max_pass, plik)
    #pliki = filtrowanie_plikow(min, max, input, output)
    print(result)
    #print("Pliki znalezione przez Thread {0}: {1}\n".format(name,pliki))
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    #for plik in pliki:

        #print(plik)
    index = 0
    for plik_th in pliki:

        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,plik_th))
        threads.append(x)
        x.start()
        index = index + 1

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)