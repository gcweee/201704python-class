def bubble(aList):
    for i in range(len(aList)):
        for j in range(len(aList)-i-1):
            if aList[j]<aList[j+1]:
                aList[j],aList[j+1] = aList[j+1], aList[j]

if __debug__ :
    aList = [3,14,0,7,8,22]
else:
    aList = []
    while True:
        input = raw_input("input a number, space for end:")
        if input == " ":
            break
        aList.append(int(input));

print aList
bubble(aList)
print aList
