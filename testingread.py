name = raw_input("enter filename: ")
if name == '': name = 'romeo.txt'
handle = open(name, 'r')
shit = handle.read()
words=shit.split()
print words
