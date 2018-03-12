from random import randint as rand
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
you_can_choose()