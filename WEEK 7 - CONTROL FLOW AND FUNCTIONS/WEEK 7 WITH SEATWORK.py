'''
shapeofyou = input("")

if shapeofyou == "square":
    print("square")
elif shapeofyou == "rectangle":
    print("rectangle")
elif shapeofyou == "circle":
    print("circle")
else:
    print("unknown shape")

print("Next Question")


myGrade = float(input("Enter your grade: "))

if myGrade >= 97:
    print("Grade/Mark: 1.0 — Excellent")
elif myGrade >= 94:
    print("Grade/Mark: 1.25 — Excellent")
elif myGrade >= 91:
    print("Grade/Mark: 1.5 — Very Good")
elif myGrade >= 88:
    print("Grade/Mark: 1.75 — Very Good")
elif myGrade >= 85:
    print("Grade/Mark: 2.0 — Good")
elif myGrade >= 82:
    print("Grade/Mark: 2.25 — Good")
elif myGrade >= 79:
    print("Grade/Mark: 2.5 — Satisfactory")
elif myGrade >= 76:
    print("Grade/Mark: 2.75 — Satisfactory")
elif myGrade == 75:
    print("Grade/Mark: 3.0 — Passing")
elif myGrade >= 65:
    print("Grade/Mark: 5.0 — Failure")
else:
    print("Incomplete / Withdrawn / Dropped")


citizenship = "Filipino"
age = 26
registered = True

if citizenship == "Filipino" and age >= 18:
    if registered:
        print("pwede ka nang bumoto")
    else:
        print("bawal kang bumoto pero you can register now")
elif citizenship == "Filipino" and age < 18:
    print("bawal kang bumoto, please wait and register")
else:
    print("bawal kang bumoto at mag register")


print("before loop")

for x in range (0, 10, 1):
    print("x value is : " + str(x))

print("after loop")

print("before loop")

for x in range(10):
    print("x value is : " + str(x))

print("after loop")

print("before loop")

for x in range(0, 10):
    print("x value is : " + str(x))

print("after loop")



fruitsList = ["Apple", "Orange", "Banana", "Pineapple"]
for fruit in fruitsList :
    print("Fruit list include : " + fruit)

print("After loop")

myString = "sana ako nalang kasi bakit mo ako iniwan dito oh"
for char in myString:
    print(char.upper())


myInfo = {
    "name": "johen",
    "age": 18,
    "favorite theory": "red string theory"
}

for key in myInfo:
    print(key + " = " + str(myInfo[key]))

for value in myInfo.values():
    print(value)


originValue = "Hello World"
print("originalValue: " + originValue)

newValue = ""

for x in originValue:
    newValue = x + newValue
    print("new value: " + newValue)

originValue = "Hello World"
reversedValue = originValue[::-1]
print(reversedValue)


print("before loop")

for i in range(10):
    if i % 2 == 0:
        print(f"{i} is an Even Number")
    elif i > 7:
        print(f"i is greater than 7: {i}")

    print("i value now is : " + str(i))

print("after loop")


import time

isConnected = False

for retry in range(4):
    print(f"Attempt {retry + 1} to connect...")


    if retry == 2:
        isConnected = True

    if isConnected:
        print("Connected successfully!")
        break
    else:
        print("Connection failed, retrying...")
        time.sleep(2)

if not isConnected:
    print("All attempts failed. Could not connect.")


for i in range(10):
    print(str(i))
    for x in range(10):
        print(x)

'''

#DECRYPTED TEXT
charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

encryptedText = "Plvv nr qd vlbd"
decrypted = ""
key = 3

for letter in encryptedText:
    if letter.isalpha():
        lowerLetter = letter.lower()
        index = charList.index(lowerLetter)
        newIndex = (index - key) % len(charList)
        newLetter = charList[newIndex]
        if letter.isupper():
            newLetter = newLetter.upper()
        decrypted += newLetter
    else:
        decrypted += letter

print("Decrypted text:", decrypted)



#ENCRYPTED TEXT
# Caesar Cipher Encryption
charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

myInput = "Miss ko na siya"
output = ""
key = 3  # shift by 3

for letter in myInput:
    if letter.isalpha():
        lowerLetter = letter.lower()
        index = charList.index(lowerLetter)
        newIndex = (index + key) % len(charList)
        newLetter = charList[newIndex]
        if letter.isupper():
            newLetter = newLetter.upper()
        output += newLetter
    else:
        output += letter

print("Encrypted text:", output)

