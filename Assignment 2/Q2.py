L = [10, 0, 20, 40, 70 ,0 , 0, 30, 0]
scores = tuple(L[:8])

# i)
print(max(scores))
print(scores.index(max(scores)))
print(min(scores))
print(scores.count(min(scores)))

# ii)
print(list(reversed(scores)))
# Tuples can not be reverse because they are immutable

# iii)
a = int(input("Enter a score"))
if a in scores:
    print("Index is ", scores.index(a))
else:
    print("Score is not in the tuple")

# iv)
try:
    scores[0] = 1000
except Exception as e:
    print(e)
# There is error because tuples are immutable while lists are not

# v)
firstScore, secondScore, *remainingScore = scores
print(firstScore)
print(secondScore)
print(remainingScore)