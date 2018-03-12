
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