L = [1, 0, 2, 4, 1, 7, 0, 0]
A = {digit * 7 for digit in L}
B = {digit * 9 for digit in L}
print(A)
print(B)

# i)
print(A.union(B))

# ii)
print(A.intersection(B))

# iii)
print(A.difference(B))
print(B.difference(A))
# difference finds elemnents strictly in first set while symmetric difference finds unique elements in both sets

# iv)
print(A.symmetric_difference(B))

# v)
print(A.issubset(B))
print(A.issuperset(B))

# vi)
X = int(input("Enter a vlue: "))
A.discard(X)
print(A)
# if element is not present in set discard() wont crash the program with an error while remove() will