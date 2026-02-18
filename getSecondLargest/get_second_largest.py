arr = [3,1,4,1,5,9,7]

def getSecLargeNum(arr):
    arrCount = list(set(arr)) #convert to set to removes duplicate and convert back to list

    if len(arrCount) < 2: 
        return None
    
    arrCount.sort(reverse=True) #sort the list in decending order
    return arrCount[1]

print(getSecLargeNum(arr))