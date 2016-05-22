#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt


fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
#gets rid of white space and puts the words in a list
	templst = line.rstrip().split()
#iterates through each word in this line
	for i in templst:
#checks to see if word is in lst
		if not i in lst:
#appends word to list
			lst.append(i)

lst.sort()
print lst
	



	
#print lst

