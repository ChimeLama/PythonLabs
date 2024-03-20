def odd():
	def is_odd_pow3(number):
		'''power = 3
		while power<number:
			power*=9
		return number==power'''
		'''if number<3:
			return False
		while number%9==0:
			number//=9
		return number==3'''
		if number<3:
			return False
		while (number*9)%3==0:
			return True
		
	
	# You can modify these to test whether your function works
	print(is_odd_pow3(0)) # should print False
	print(is_odd_pow3(0.5)) # should print False
	print(is_odd_pow3(1)) # should print False
	print(is_odd_pow3(3)) # should print True
	print(is_odd_pow3(9)) # should print False
	print(is_odd_pow3(27)) # should print True
	print(is_odd_pow3(243)) # should print True
	print(is_odd_pow3(300)) # should print False
