n = input("Enter a string: ")
output = []
for i in range(len(n)-1, -1, -1): #loop from last index of n (len(n)-1) to 0 
    output.append(n[i]) #take the characters from i and add it to output. since i start from -1, the letters will be added from the end of the string
print("".join(output)) #join all the character