from random import randint as rand 
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


def you_can_choose(): 
	print "Now You entered the funniest room"
	print "I am going to pick number from 0 to 50 and You will guess the number "
	print "If yuo guess the right answer you scores will increase "
	print "If you gues the wrong answer I will give you a hint "

	def choose_number():
		
		score = 0
		computer_choice = rand(0,51)	
		while score <=100:
			
			user_guess= int(raw_input("Can you guess the number I picked: "))
			if user_guess == computer_choice:
				score +=1
				print "Wow you won, Conglatulations!!!"		
				
				if score>=50:
					print "Wow!!! You are a good player"
				elif score<50:
					print "Continue to enjoy the game!!!"
				elif score==100:
					print "You are great now you can be a good soldier"
				else:
					"good job!!"
				break				
						
			elif user_guess>computer_choice:
				print "Oooh, guess lower: "
			elif user_guess<computer_choice:
				print "Oooh, guess higher"
			else:
				print "I am not sure about the number you typed in "
	score =0
	while score <=100:
		choose_number()
		score +=1
		print "Your score now is %s "%score

def personalInformation():
	print "Now we are going to build your personal story of your choice. "
	name =str(raw_input("What is your name?  "))
	age= int(raw_input("How old are you? "))
	district = str(raw_input("What is your home district? "))
	animal = str(raw_input("What is your favorite animal? "))
	verb = str(raw_input("write any verb you want: "))
	adjective = str(raw_input("Can you write any adjective you want: "))

	age_days=age*365
	print "......................................."
	print "Hey I know who you are. "
	print "You are %s, %s days old, \n and you are from %s district"%(name,age_days,district)
	print "You know what,,,, you %s %s "%(verb, adjective)
	print "......................................."

print "In this house we have three rooms: "
print "\t>calculation room where you can do mathematics"
print "\t>Personal information room "
print "\t>Picking rondom number room "
print "Here is the instructions"
print "\tIf you want to enter in calculation room\n write calculation"
print "\tIf you want to enter in personal information room \n write information"
print "\tIf you want to guess numbers \n write guess"

def user_choose():
	user_make_choice=str(raw_input("Which room you want to enter in: "))
	if user_make_choice=="calculation":
		calculator()
	elif user_make_choice=="information":
		personalInformation()
	elif user_make_choice=="guess":
		 you_can_choose()
	else:
		print "It is seems like you don't like me!!!\n But you can retry"
		user_choose()

user_choose()
