x = int(input("Enter Your 1st Side\n"))
y = int(input("Enter Your 2nd Side"))
z = int(input("Enter Your 3rd Side"))

if (x > 0 and y > 0 and z > 0):


    if x == y and y  == z:
        print("THis is equlateral")

    elif x == y or y == z:
        print("triangle is isoseceles")

    else:
        print("Scalene")

else:
    print("This is not a triangle")
