def room():
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = float(input("Enter side C: "))
    d = float(input("Enter side D: "))
    e = float(input("Enter side E: "))
    rect1 = (a * b)
    rect2 = (d - b - e) * (a - c)
    tri = (a - c) * e * 0.5
    print("Room Area: " + str(rect1+ rect2+tri))
