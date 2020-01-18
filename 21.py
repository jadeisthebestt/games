import random

print ("21 time baby!")

score = 0
while True:
	highest_number = 0
	while highest_number < 21:
		num_1 = int(input ("You go first.Pick a number between " + str(highest_number+1) + " and " + str(highest_number+2) + "   "))
		highest_number = num_1
		if highest_number == 21:
			print ("You won the game!! Well Done!")
			score = score +1
			print ("")
		highest_number = random.randint(1,2) + num_1 
		print (highest_number)

	if highest_number == 21:
		print ("Haha! I won you lost!")
		score = score -1


























