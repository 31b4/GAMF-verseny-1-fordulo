globalCounterA = 0
globalCounterC = 0
bAnsw = 0
def PrimeE(num):
    if num == 4:
        return False
    for i in range(2, num//2):
        if (num % i) == 0:
            return False
    return True
for num in range (10,100000):
    prime = True
    prime = PrimeE(num)
    if prime:
        globalCounterA += 1
        bAnsw = num
        sumOfNum =0
        for char in str(num):
            sumOfNum += int(char)
        if PrimeE(sumOfNum):
            globalCounterC +=1
print("a: ", globalCounterA)
print("b: ", bAnsw)
print("c: ", globalCounterC)