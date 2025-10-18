isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86
isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)
isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)
isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed)