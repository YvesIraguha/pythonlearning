
import random

# return a full name of a user provided first name and last name
def full_name():
  first_name=input("Enter your first name")
  last_name=input("Enter your last name")
  return first_name+" "+last_name

#count the number of legs in a farm provided number of chickens, dogs, and pigs
def animals(chickens,dogs,pigs):
  return chickens*2 + dogs*4 + pigs*4

#convert minutes to seconds
def convert_to_seconts(minutes):
  return minutes*60


#count a number of arguments a function was called with
def count_args(*args):
  return len(args)

#lottery app 

# check a winning number
def winning(num):
  digits = str(num)
  total = 0
  for i in digits:
    total += int(i)**2
  if (total == 4):
    return False
  elif (total == 1):
    return True
  else:
    return winning(total)

#generate 20 random numbers, with 3 winning numbers only, and no repetition. 
def lottery():
  random_numbers =[]
  winning_numbers = []
  while len(winning_numbers)<3:
    random_number = random.randint(100,1000)
    if(winning(random_number)):
      winning_numbers.append(random_number)
      random_numbers.append(random_number)
    else:
      continue
  
  while len(random_numbers) < 20:
    new_random_number = random.randint(100,1000)
    if (winning(new_random_number)):
      continue
    elif (new_random_number in random_numbers):
      continue
    else:
      random_numbers.append(new_random_number)
   
  print ('winning numbers',winning_numbers)
  print('all numbers',random_numbers)
  return random_numbers
    
  

lottery()
