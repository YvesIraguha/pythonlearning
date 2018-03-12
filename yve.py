
i=0
numbers=[]
for i in range(0,10):

	
	numbers.append(i)
	print numbers
	i +=1

i=10
numbers=[0,1,2,3,4,5,6,7,8,9,10]
for x in range(0,10):	

	numbers.pop(i)
	print numbers
	i -=1
def check_is_even(number):
	if number%2==0:
		print "Yes this number %r is even" %number
	elif number%2!=0:
		print "It is odd"
	else:
		print "Bastard what are you doing."
check_is_even(13)


def lentgh_of_string():
	string = raw_input("write something :")
	
	res = 0
	for letter in string:
		res +=1

	print "The length of the string you entered is %s"%res
	print letter 
	print string[-1]

lentgh_of_string()

def who_is_the_bigger_guy():
	first_number = float(raw_input("Enter the first number: "))
	second_number = float (raw_input("Enter the second number: "))

	if first_number>=second_number:
		print first_number
	else:
		print second_number

who_is_the_bigger_guy()

# while x<5:
# 	print x
# 	print "her hey the number is %s"%x

# 	x +=1

# def my_function():
# 	i=0
# 	numbers=[]
# 	for i in range(0,10):

		
# 		numbers.append(i)
# 		print numbers
# 		i +=1
# 		if i==5:
# 			continue 
# 		elif i==9:
# 			break

# my_function()