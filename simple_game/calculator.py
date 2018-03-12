
def calculator():
	print "Welcome to caclcualator \n you can calculate any number you want"
	print "Here there are many operations."
	print "write add to add two numbers"
	print "Write multiply to multiply two numbers"
	print "Write divide to make division of two numbers"
	print "Write substract to substract one number from another"
	print "Write remainder to know the \n remainder of division of one number with another"
	print "Write square to square a number. "

	def addition():
		first_number=float(raw_input("Enter the first number: "))
		second_number = float(raw_input("Enter the second number: "))
		result = first_number + second_number
		print "From the calculation the result is %s "%result 

	def substraction():
		first_number=float(raw_input("Enter the first number: "))
		second_number = float(raw_input("Enter the second number: "))
		result = first_number - second_number
		print "From the calculation the result is %s "%result 

	def multiplication ():
		first_number=float(raw_input("Enter the first number: "))
		second_number = float(raw_input("Enter the second number: "))
		result = first_number * second_number
		print "From the calculation the result is %s "%result 

	def division ():
		first_number=float(raw_input("Enter the first number: "))
		second_number = float(raw_input("Enter the second number: "))
		result = first_number / second_number
		print "From the calculation the result is %s "%result 

	def squaring():
		first_number=float(raw_input("Enter the first number: "))
		second_number = float(raw_input("Enter the second number: "))
		result = first_number ** second_number
		print "From the calculation the result is %s "%result 

	def remainder():
		first_number=float(raw_input("Enter the first number: "))
		second_number = float(raw_input("Enter the second number: "))
		result = first_number % second_number
		print "From the calculation the result is %s "%result 

	def calculation():
		user_command = str(raw_input("Can you write your operation: "))

		if user_command== "add":
			addition()
		elif user_command=="multiply":
			multiplication()
		elif user_command== "divide":
			division()
		elif user_command=="substract":
			substraction()
		elif user_command=="remainder":
			remainder()
		elif user_command=="square":
			squaring()
		else:
			print "Incorrect operation!"
		move_out = str(raw_input("Do you want to make more calculation: "))

		if move_out == "yes":
			calculation()
		else:
			print "Thank you for using this awesome calculator"

	calculation()
calculator()
