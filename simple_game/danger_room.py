from random import randint as rand
import random

print "The room here is full of gold!"
print "However to have the gold you need to fight for it."
print "In the corridor there are many directions to take"
print "Make the right choice in order to enter: "

score =0

directions = ["right","left","down","up"]
lions =["kill","Taunt","still","hurt","remove"]
lion=random.choice(lions)
number = rand(0,4)
direction= random.choice(directions) 

print "There are four directions {name}, pick one "{name = directions}
print directions
user_direction=str(raw_input("Can you choose direction among the direction methioned: "))

if user_direction==direction:
	score +=3
	print "You did the right choice \n Here is the lion can you select among this choice what you will do"
	user_lion=str(raw_input("what choice you made?"))

	if user_lion==lion:
		print "You are dead and You can not continue"
	elif user_lion != direction:
		score+=3
		print "Your current score is %s \n and You can continue" %score
		number_of_gold=int(raw_input("how many kilograms of gold you want to take: "))

		if number_of_gold<5:
			score +=15
			print "Your curernt score is %s "%score
			print "Good now You are not gridy take %s kilograms "%score
		else:
			print "Bastard take few gold."
	else:
		print "What are you doing"


