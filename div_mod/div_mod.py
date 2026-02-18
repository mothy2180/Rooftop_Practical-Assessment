x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

quotient = 0
remainder = x

if y == 0 :
    print("Value of x must be bigger than value of y")

while remainder >= y:
    remainder = remainder - y
    quotient = quotient + 1
    print("The remainder of this calculation is ", remainder)
    print("The quotient for this calculation is ", quotient)
