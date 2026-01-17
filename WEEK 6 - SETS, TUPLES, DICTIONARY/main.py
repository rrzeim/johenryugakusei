mgapumasangintellects = ["johen", "red", "vince"]
print(mgapumasangintellects)

print(mgapumasangintellects[2])

isThere = "individual" in mgapumasangintellects
print(isThere)

mgapumasangintellects.append("de leon")
print(mgapumasangintellects)

mgapumasangintellects.insert(0, "ryugakusei")
print(mgapumasangintellects)

print(len(mgapumasangintellects))

print(mgapumasangintellects.count("de leon"))
print(mgapumasangintellects.count("glydelmatias"))
mgapumasangintellects.remove("johen")
print(mgapumasangintellects)
print(mgapumasangintellects.index("de leon"))
mgapumasangintellects[3] = "glydelmatias"
print(mgapumasangintellects)


fA = ["ferrari", "mercedes", "astonmartin"]
fB = ["ferrari", "mclaren", "astonmartin"]
fC = ["redbull", "mclaren", "astonmartin"]


f_list = [fA, fB, fC]
print(f_list)


f_list_combined = fA + fB + fC
print(f_list_combined)


fA.extend(fB)
fA.extend(fC)
print(fA)

print(f_list[2][1])


colorsA = {"red", "red", "blue", "yellow"}
colorsB = {"red", "maroon", "purple", "yellow"}

print(colorsA)
print(colorsA)
print(colorsA)

colorsA.add("gray")
print(colorsA)

colorsUnion = colorsA.union(colorsB)
print(colorsUnion)
colorsIntersection = colorsA.intersection(colorsB)
print(colorsIntersection)
colorsDifference = colorsA.difference(colorsB)
print(colorsDifference)

colorslistofSet = [colorsA, colorsB]
print(colorslistofSet)


drinksA = ("coke", "sprite", "royal")
print(drinksA)

print(drinksA.index("royal"))
print(drinksA.count("coke"))

print(drinksA[2])

print(drinksA[-1])

drinksB = ("beer", "rootbeer", "orangebeer")
drinksbasket = (drinksA, drinksB)
print(drinksbasket)

mytuple = (
    (1, 2, 3, "A"),
    (4, 5, 6, "B"),
    (7, 8, 9, "C"),
)

print(mytuple)
print(mytuple[2][3])

myInfo = {"Name": "Johen Ryugakusei", "FavTopic": "Thermodynamics", "FavoriteSubject": "CHEM015"}
print(myInfo)
print(myInfo["FavoriteSubject"])
print(myInfo["FavTopic"])

print(myInfo.get("FavoriteSubject"))

myInfo["Name"] = "Edna E mode"
print(myInfo)
myInfo.update({"License": "Chemist"})
print(myInfo)

myInfo = {
    "Personal": {
        "Name": "Johen Ryugakusei",
        "Age": 18,
        "FavoriteColor": "Blue"
    },
    "Education": {
        "HighSchool": "PNHS",
        "University": "PUP",
        "Degree": "Electronics Engineering"
    },
    "License": {
        "Type": "Engineer",
        "YearIssued": 2029
    }
}

print(myInfo)


print(myInfo["Personal"]["Name"])
print(myInfo["Education"]["Degree"])
print(myInfo["License"]["YearIssued"])