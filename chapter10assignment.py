#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
#goes through each line
for line in handle:
#checks for From in each line, and skips if it doesn't have it
	if not 'From ' in line: continue
#splits into lists of words
	words = line.split()
#splits the time into hour minute seconds
	word = words[5].split(':')
#puts the hours into a dict with the corresponding counts
	count[word[0]] = count.get(word[0], 0) + 1

#sorts through the list of tuples and prints
for k,v in sorted(count.items()):
	print k,v

		
