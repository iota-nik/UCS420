import random
from collections import Counter

random.seed(1024170030)

# i)
randomList = [random.randint(100, 900) for i in range(100)]

# ii)
oddNumbers = [x for x in randomList if x%2 != 0]
print(oddNumbers)
print(len(oddNumbers))

# iii)
evenNumbers = [x for x in randomList if x%2==0]
print(evenNumbers)
print(len(evenNumbers))

# iv)
def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

primeNumbers = [x for x in randomList if isPrime(x)]
print(primeNumbers)
print(len(primeNumbers))

# v)
mostFreq, count = Counter(randomList).most_common(1)[0]
print(mostFreq)
print(count)