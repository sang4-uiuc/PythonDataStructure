#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#goes through each line
counts = dict()
for line in handle:
#checks if it has From and skips if it doesn't
	if not "From " in line: continue
#splits the line into words 
	words = line.split()
#checking to see if the email which is word[1] appears in the line, if not the count gets set to 1
	counts[words[1]] = counts.get(words[1],0) + 1	
		
#set the max to none
maxemail = None
maxcount = None
#iterate through the dictionary
for email, occurence in counts.items():
#sets the max to the count that's the largest
	if maxcount is None or occurence > maxcount:
		maxcount = occurence
#sets the maxemail to the corresponding email
		maxemail = email

print maxemail, maxcount
