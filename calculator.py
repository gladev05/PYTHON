print("This is your calculator\n")

x = float(input("Please Enter your first value: \n"))
y = float(input("Please enter Your secound Value: \n"))

print("Which Operation You Want to Perform")

print("--> 1 = |+| \n -> 2 = |-| \n -> 3 = |*| \n -> 4 = |%|")
cal = float(input("Your Operation Value \n"))
print("You Opted For option -->", cal)

if cal == 1:
    print( x + y )
   
elif cal == 2:
    print( x - y)

elif cal == 3:
    print( x * y)

elif cal == 4:
    print( x / y)
