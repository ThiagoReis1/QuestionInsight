from numpy import *
notas = array(eval(input('notas: ')))
media = [5,4,3,2]
num = (notas * media)
num1 = sum(num)
den = sum(media)
medp = (num1/den)
print(round(medp, 2))