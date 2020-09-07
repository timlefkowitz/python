#Reading_*the_Whole*_File
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])
