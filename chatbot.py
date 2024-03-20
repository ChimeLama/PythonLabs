def chat():
    name=input("What is your first name?")
    import random
    
    ra = random.randint(1, 3)
    
    if  ra==1 :
    
       print("HIII " + name + " Nice to meet you!!")
       
    elif ra==2 :
    
       print("Hellor " + name)
    
    else:
    
       print("I love your name ")
    
    
    age=int(input("How old are you?"))
    if age< 18:
        print(str(age) +" is a good age to start exploring style.")
    elif age ==1:
        print("You are 1 how are you able to write:0")
    else:
        print( str(age) + " is cool")
    shirt=input("What kind of clothes do you wear on a daily basis?")
    if shirt=="gothic":
        print("I aspire to be you!")
    elif shirt=="lolita":
        print("I have been trying to get into lolita but so expensive :{")
    else:
        print("Oh " + shirt + " that's cool i mostly wear shirts and pants.")
    style=input("If you could describe your style or what you aim what is it?")
    print("That's so coool")
    feel=input("How are you feeling?")
    if feel=="happy":
        print("I am happy you're happy")
    elif feel=="sad":
        print("I am sad you're sad")
    else:
        print("Oh i see!")
    
    print("Anything you wanna to add?")
    
    next=input("")

    import random
    
    r = random.randint(1, 3)
    
    if r==1:
    
       print("You are amzing ")
    
    elif r==2 :
    
       print("Interesting. ")
    
    else:
    
       print("How weird. ")
    
    print("Well, " + name + ", it has been nice chatting with you.")
