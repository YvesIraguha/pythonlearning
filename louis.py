from sys import argv

script, firstfile, secondfile=argv

print "I am going to read %s \n then I will copy the content in it \n and put it into %s."%(firstfile,secondfile)
text =open(firstfile)
indata=text.read()

print "let's copy something here"
my_text=open(secondfile, "w")
my_text.write(indata)

my_text.close()
text.close()