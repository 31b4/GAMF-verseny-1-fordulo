with open('f1Input.txt') as f:
    lines = f.readlines()
pm = True
globalCountA = 0
globalCountB = len(lines)/91
globalCountC = 0
for x in lines:
    if int(x) == 5:
        globalCountA +=1
    if pm:
        globalCountC += int(x)
    else:
        globalCountC -= int(x)
    pm=not pm
print("a: ",globalCountA)
print("b: ",globalCountB)
print("c: ",globalCountC)