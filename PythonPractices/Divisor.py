__author__ = 'adisr21'

num = int(input("Please choose a number to divide: "))

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    divisorList.append(number)

print(divisorList)
