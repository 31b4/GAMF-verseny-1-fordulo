with open('f2Input.txt') as f:
    lines = f.readlines()
globalCounterA = 0
globalCounterB = 0
globalCounterC = 0

def asd(word,letter):
    for char in word:
            if char ==letter:
                return 1
    return 0
for row in lines:
    for char in row:
        if char.lower() == 'i':
            globalCounterA +=1
    for word in row.split(' '):
        for i in range(len(word)-4):
            if word[i] == 'i' and word[i+3]=='a' and word[i+4]=='n':
                globalCounterB +=1
        validCount = asd(word,'i')
        validCount += asd(word,'a')
        validCount += asd(word,'n')
        if validCount == 2:
            globalCounterC += 1
print("a: ",globalCounterA)
print("b: ",globalCounterB)
print("c: ",globalCounterC) 
