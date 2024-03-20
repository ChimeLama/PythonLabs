def thrr():
    intut=int(input("How many numbers do you need to check? "))
    div3=0
    undiv=0
    for i in range(intut):
        ent=int(input("Enter number: "))
        if ent%3==0:
            print(str(ent)+ " is divisible by 3.")
            div3+=1
        else:
            print(str(ent) + " is not divisible by 3.")
            undiv+=1
    print("You entered "+str(div3)+ " number(s) that are divisible by 3.")
    print("You entered " + str(undiv) +" number(s) that are not divisible by 3.")
