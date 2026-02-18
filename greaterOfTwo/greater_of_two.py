x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
while x > y :
    print(x)
    break
else:
    while y > x: 
        print(y)
        break
    else :
        print("Both numbers are equal")
