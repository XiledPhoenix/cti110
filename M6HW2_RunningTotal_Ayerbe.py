#CTI-110
#M6HW2 - Running Total
#Guillermo Ayerbe
#12-4-2017

total = 0
for x in range(int(input('How many scores will you enter? '))):
    score = int(input('Enter your test score. '))
    total += score

print('Your total is ',total)
