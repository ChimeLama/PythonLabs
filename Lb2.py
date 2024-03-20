def change():
	p = int(input("Enter the number of pennies: "))
	n = int(input("Enter the number of nickels: "))
	d = int(input("Enter the number of dimes: "))
	q = int(input("Enter the number of quarters: "))
	l = int(input("Enter the number of loonies: "))
	t = int(input("Enter the number of toonies: "))
	
	# totaltotal_value = ...
	
	
	
	total_value=(p + 5*n + 10*d + 25*q + 100*l +200*t)/100
	
	
	
	
	
	print()  # this prints a blank line
	print("Number of pennies:", p )
	print("Number of nickels:", n)
	print("Number of dimes:", d)
	print("Number of quarters:", q)
	print("Number of loonies:", l)
	print("Number of toonies:", t)
	print("Total value of coins: $" + "{:.2f}".format(total_value))
	
	# print("Total value of coins: $" + str(total_value))