
intA = 555
intB = 5
intC = 4

isDivisible = False #initial value
remainder = intA % intB #modulus or the percent sign returns the remainder
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

isDivisible = False #initial value <--------------------------------------
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)