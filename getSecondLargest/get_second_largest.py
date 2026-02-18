arr = [3,1,4,1,5,9,7]

def getSecLargeNum(arr):
    arrCount = list(set(arr))

    if len(arrCount) < 2:
        return None
    
    arrCount.sort(reverse=True)
    return arrCount[1]

print(getSecLargeNum(arr))