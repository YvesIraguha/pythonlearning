from sys import argv #the method here import argv
script, filename=argv #it stores the variable to be called next time
txt=open (filename)# the line stores an opened file in a variable called txt
print "here's your file %r:"%filename  #the line have a formatter which calls the name of the file. 
print txt.read() # it prints the file in read more so that we can read the content of the file. 
 
print "Type the filename again:" # it prints another staffs
file_again=raw_input(">")     # it prompt the user to write something and then are stored.
txt_again=open(file_again) # the file is then opened and store into another variable. 

print txt_again.read() # the  line prints again the file in read form. 