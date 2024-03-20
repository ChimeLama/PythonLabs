import random
def gen():
	def passGen():
	    listOfAnimals=["tiger", "cat" , "dog, platypus" , "elephant", "red panda", "racoon" , "snake" ]
	    ani=random.choice(listOfAnimals)
	    beginNum=random.randint( 7,89029)
	    lastNum=random.randint(1,500)
	    listofChar=["<", "@", "/", "*"]
	    char=random.choice(listofChar)
	    newPass= str(beginNum)+ani+ str(lastNum) + char
	    print(newPass)
	passGen()
"""
The function name is passGen( ).This function is tasked with making a random password that uses a random list of numbers from 7-89029, random animals,another random number and list of characters.
"""