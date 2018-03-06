# from sys import argv
# # import exist

# script,firstfile,secondfile=argv
# print "the script is %r, the name for the first file is %r and the second file is %r"%(script,firstfile,secondfile)

# pacy=open(firstfile,"r")
# aphro=open(secondfile,"w")

# def copy(x,y):
# 	print x
# 	print y
# 	y.write(x)

# copy(pacy,aphro)


print "now we are going to calculate some stuffs:"

pacy=raw_input("write some number: ")
aphro=raw_input("write other number: ")

pros=float(pacy)
birtin=float(aphro)

def addition(x,y):
	print x*y

def multiplication(x,y):
	print x+y

yves=raw_input("write addition to multiply and multiplication to add")
if yves=="addition":
	addition(pros,birtin)
else:
    multiplication(pros,birtin)

