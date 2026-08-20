myDict = {
    "name" : "Nikunj",
    "rollNo" : 1024170030,
    "branch" : "COPC",
    "age" : 19,
    "city" : "Yamunanagar"
}

# i)
myDict["location"] = myDict.pop("city")

# ii)
myDict["CGPA"] = 9.18

# iii)
myDict["age"] += 1

# iv)
myDictCopy1 = myDict.copy()
myDiictCopy2 = myDict.copy()

poppedBranch = myDictCopy1.pop("branch")
del myDiictCopy2["branch"]
# pop() removes key and returns the value while del removes both key and value and returns nothing

# v)
for key, value in myDict.items():
    print(f"{key} -> {value}")

# vi)
if "email" in myDict:
    print(myDict["email"])
else:
    print("Safe Fallback")

# vii)
friendDict = {
    "name" : "Obi Wan kenobi",
    "rollNo" : 10770077,
    "branch" : "Jedi Master",
    "age" : 21,
    "city" : "Coruscant"
}
mergedDict = {**myDict, **friendDict}
# when mergeing 2 dictionaries and both share a key, dictionary placed on the right wins and other is overwritten

# viii)
stringDict = {k: v for k, v in myDict if isinstance(v, str)}