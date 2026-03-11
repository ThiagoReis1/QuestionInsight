from numpy import *
notas = array(eval(input('notas: ')))
media = [1,2,3]
num = (notas * media)
num2 = sum(num)
den = sum(media)
med = (num2 / den)
print(round(med, 2))