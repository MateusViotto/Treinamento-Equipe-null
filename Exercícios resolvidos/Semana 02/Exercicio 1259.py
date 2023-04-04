i = int(input())
numberList = []
numberListEven = []
numberListOdd = []

for x in range(i):
    number = float(input())
    numberList.append(number)

for y in numberList:
    if y % 2 == 0:
        numberListEven.append(y)
    else:
        numberListOdd.append(y)

numberListEven.sort()
numberListOdd.sort(reverse = True)

for a in numberListEven:
    print( "%d" % a)

for b in numberListOdd:
    print( "%d" % b)