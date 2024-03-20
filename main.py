#importing functions
from Lb2 import change
from Lb4 import gen
from Lb5 import check
from Lb6 import leap
from sillysentence import silly
from arearoom import room
from div import thrr
from Lb7 import age
from Lb8 import pyramid
from Lb9 import odd
from chatbot import chat
from cat import cat
from calendar import calender
from personal import organizer 
#end of import
#starts game
print("Welcome to my portfolio")
print("============================")
print("============================")
portfolio_state=True

#listing options of lab
while portfolio_state == True:
	print("Labs: ")
	print("1. Silly Senteces")
	print("2. Labs 1 and 3(Not available)")
	print("3. Coin Calculate")
	print("4. Project STEM Calculate Area of room")
	print("5. Password generator")#no
	print("6. Input checker")
	print("7. Project STEM ChatBot")#no
	print("8. Project STEM Divisible by 3")
	print("9. Do now ASCII cat or pinguin")#idk
	print("10. Leap year check")
	print("11. Age Related Conditions")
	print("12. Number Pyramids ")
	print("13. Odd power of three")
	print("14. Calendar")
	print("15. Personal Organizer")

	lab_choice= input("Which lab do you want to see?(1 to 15)? ")

	#directing numbers to correct lab
	if lab_choice=="1":
		silly()
	elif lab_choice=="2":
		print("Its not available because it uses PyGame.")
	elif lab_choice=="3":
		change()
	elif lab_choice=="4":
		room()
	elif lab_choice=="5":
		gen()
	elif lab_choice=="6":
		check()
	elif lab_choice=="7":
		chat()
	elif lab_choice=="8":
		thrr()
	elif lab_choice=="9":
		cat()
	elif lab_choice=="10":
		leap()
	elif lab_choice=="11":
		age()
	elif lab_choice=="12":
		pyramid()
	elif lab_choice=="13":
		odd()
	elif lab_choice=="14":
		calender()
	elif lab_choice=="15":
		organizer()
		print("Personal organizer Executed")
	#making sure wrong numbers don't stop the program
	else:
		print("Not a valid number")
	#allowing user to continue or not
	playAgain=input("Wanna keep going?(y/n): ")	
	if playAgain!="y":
		portfolio_state=False
		print("")
print("Thx")

	