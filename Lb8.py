def pyramid():
	height = input("Enter an integer between 1 and 5: ")
	if height.isdigit() and 0<int(height)<=5:
		height=int(height)
		for i in range(height):
			row=i+1
			print(" "*2*(height-row),end="")
			for r in range(row,2*row):
				print(str(r) +" ", end="")
			print()
	else:
		print("That's not an integer between 1 and 5")
