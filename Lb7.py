#age is lees than 16 can't drive, 16 cann get permit but with superviion until 18 ,can get liscense at 18 , 21 can supervise with liscense
def age():
	age=int(input("Enter your age to determine if you are allowed to drive, vote and see age restricted movies: "))
	#drive
	
	if age == 16 and age == 17:
		print("You can get a learners permit and only drive with a liscensed supervisor that is 21+ , cant vote , can watch G rated ")
	if age ==18 and age ==19 and age ==20:
		print("You can drive without supervision!")
	if age >=21:
		print("You can drive and be a supervisor to those younger than 18 who are driving")
	else:
		if age < 16:
			print("You are too young to drive")
	#vote
	if age >= 18:
		print("You can vote")
	else:
		print("You cant vote yet")
	
	#movies
	if age > 0:
		print("You can watch G rated movies")
	if age < 13:
		print("You can watch PG rated movies")
	if age >=13:
		print("You can watch pg movies  ")
	if age >=17:
		print("You can watch r movies  ")
	if age >=18:
		print("Can watch X rated movies")

