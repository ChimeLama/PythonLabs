def check():
	input_1 =input("Enter a 4-digit whole number: ")
	if len(input_1)==4 and (input_1).isdecimal() and input_1[0] !="0":#[0 is the index]
	  print("Thanks!")
	else:
	  print("That's not a 4-digit whole number.")
	#input_1 = int(input("Enter a 4-digit whole number: "))
	#if input_1  >=1000 and input_1 <=9999:
	input_2 = input("Enter an integer less than 50: ")
	if (input_2.isdecimal() or (input_2[1:].isdecimal and input_2[0]=="-")) and int(input_2)<50:
		print("Thanks!")
	else:
	  print("That's not an integer less than 50.")
	
	input_3 = input("Enter a string that begins with a vowel: ")
	if input_3[0].lower() in "aeiou":
		print("Thanks!")
	#v=["A","E","I","O","U"]
	#if input_3.startswith(tuple(v)):
	#  print("Thanks!")
	#else:
	 # print("That does not begin with a vowel.")
	
	input_4 = input("Enter a string that ends with a consonant: ")
	if input_4[-1].isalpha() and input_4.lower()not in "aieou":
		print("Thanks!")
	else:
		print("That does not end with a consonant.")
	#cons=["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", #"S", "T", "V", "W", "X", "Y", "Z","b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
	#if input_4.endswith(tuple(cons)):
	 # print("Thanks!")
	#else:
	#  print("That does not end with a consonant.")
	  