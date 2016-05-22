#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
#parses through each line
for line in fh:
#checks if the line starts with From:
	if not "From:" in line:
#if it doesn't then we skip
		continue
#if it does we split it into a list
	lst = line.split()
#the email is the second word in the list
	email = lst[1]
	print email
#add count
	count +=1

print "There were", count, "lines in the file with From as the first word"

