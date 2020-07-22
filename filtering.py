
# Iterating over each line in the file using for in loop

# with open("password.dat") as file_handle:
#     for line in file_handle.readlines():
#         print(line, end='')
min_pass = 5
max_pass = 15

def min_max_pw(min, max, input, output):
    source_file = open(input, "r")
    dest_file = open(output, "w")
    for line in source_file:
        if len(line) > min and len(line) < max:
            dest_file.write(line)


min_max_pw(5,15,"password.dat","password2.dat")

def duplicate_pw(input, output):
    with open(input) as result:
        uniqlines = set(result.readlines())
        with open(output, 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

duplicate_pw("password2.dat","password3.dat")



source_file = open("password.dat", "r")
print("Source:")
print(source_file.read())
print()
print("Dest:")
dest_file = open("password3.dat", "r")
print(dest_file.read())
dest_file.close()

