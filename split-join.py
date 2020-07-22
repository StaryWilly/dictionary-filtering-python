#I named the accumulative file common.doc to distinct from the other .txt files in the target directory. Also, this example code #implies all the files are in the same directory.

# merging.py
import os
import glob

with open("common.doc", "w") as common:
    for txt in glob.glob("./*.txt"):
        with open(txt, "r") as f:
            content = f.read()
        common.write("{} ({})\n".format(os.path.basename(txt), content))

#And after common.doc editing:

# splitting.py
with open("common.doc", "r") as common:
    for line in common:
        name = line[:line.find(" (")]
        text = line[line.find(" (")+2:line.rfind(")")]
        with open(name, "w") as f:
            f.write(text)

#And a solution for multiline text (merging stays with .strip() removed on content writing), not suitable for hundreds of thousands of #files tho...

# splitting2.py
with open("common.doc", "r") as common:
    everything = common.read()
elements = everything.split(")")
for elem in elements:
    name = elem[:elem.find(" (")].strip()
    text = elem[elem.find(" (")+2:]
    if name:
        with open(name, "w") as f:
            f.write(text)


