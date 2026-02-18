n = "parallel"

def firstUniqChar(word):
    charCount = {}
    for char in word:
        charCount[char] = charCount.get(char,0) + 1

    for char in word:
        if charCount[char] == 1:
            return char
        
    return None

print(firstUniqChar(n))