n = "parallel"

def firstUniqChar(word):
    charCount = {} 
    for char in word:
        charCount[char] = charCount.get(char,0) + 1 #count the frequency of a character and default value is 0

    for char in word:
        if charCount[char] == 1: #find the value with frequency = 1
            return char
        
    return None

print(firstUniqChar(n))