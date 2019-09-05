import re  				 # A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
						 #Python has a built-in package called re, which can be used to work with Regular Expressions.



f=open("file.txt")   	# In Python, there is no need for importing external library to read and write files. Python provides an inbuilt function for creating, writing and reading files.
						 #The open() function takes two parameters; filename, and mode.
						 #There are four different methods (modes) for opening a file:

						 #"r" - Read - Default value. Opens a file for reading, error if the file does not exist

						 #"a" - Append - Opens a file for appending, creates the file if it does not exist

						 #"w" - Write - Opens a file for writing, creates the file if it does not exist

						 #"x" - Create - Creates the specified file, returns an error if the file exists
content=f.read()		#The open() function returns a file object, which has a read() method for reading the content of the file.
						# the read() method returns the whole text.

f.close()   			#when we used the file we need to close the file using Close() method.


f1=open("email.txt","w+")  #open a file in write mode if the file is not present then it will create the file by the given  name, mentioned in the write method.
s=re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",content) #thiis will check every word weather the word fulfill the condition of being an email. 
																		 # If yes the it will extract that word and append in the list, and check for all other words.
t=('\n'.join(s))      # it will convert the list into string because  write method takes string as argument to write in the file.
f1.write(t)   		  #used to write the string in the file.
f1.close() 			  # close the file using close().
