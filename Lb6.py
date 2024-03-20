def leap():
	year = int(input("Enter a year: "))
	#leap year is an extra day in feburary every 4 years
	#If you were born on feb 29 you can only celebrate your birthday every four years on that day
	#tropical day 365 days 5 hr 48 min 45 sec 138 ms
	#every fouryears make it leap isjulian calender
	# f the year is multiple of 100 not a leap yr
	# f the year is multiple of 400 is a leap yr
	#if multiple of 10 thousand or 10 thousand + 2800 not leap yr
	# if the year ends in 2800 or 5600 or 8400 then not a leap yr
	if year <= 1752: # start of the gregoriann calender
	  print("There was no leap year!!")
	elif year > 10000 and (year - 2800)%10000==0 and (year%100)==0:
		print(year , "it was not a leap year ")
	
	
	elif year <10000 and (year-2800)%10000==0:
		print(year, "It is a leap year")
	elif year < 10000 and (year-5600)%10000==0:
		print(year, " it is not leap year")
	elif year < 10000 and ( year-8400)%10000==0:
		print(year , "not leap yr")
	else:
		if year %400 == 0:
			print( year, "Its a leap year")
		elif year%100!=0 and year %4==0:
			print(year, "Its a leap year")
		else:
			print("not a leap year")
	
	#age is lees than 16 can't drive, 16 cann get permit but with superviion until 18 ,can get liscense at 18 , 21 can supervise with liscense