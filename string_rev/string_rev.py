n = input("Enter a string: ")
output = []
for i in range(len(n)-1, -1, -1):
    output.append(n[i])
print("".join(output))