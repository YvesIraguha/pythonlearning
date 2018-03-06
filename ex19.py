def Cheese_and_crackers(cheese_count,boxes_of_crackers):
	print"you have %d cheeses!"%cheese_count
	print "You have %d boxes of crackers"% boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
Cheese_and_crackers(20,30)

print 'OR, we can use variables from our script:'
amount_of_cheese=10
amount_of_crackers=20


Cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print "We can even do math inside too:"
Cheese_and_crackers(10+20,5+6)

print"And We can combine the two, variables and math:"
Cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)