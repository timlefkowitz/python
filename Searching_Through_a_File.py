#Searching_Through_a_File line=line.rstrip() takes the newline out
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
