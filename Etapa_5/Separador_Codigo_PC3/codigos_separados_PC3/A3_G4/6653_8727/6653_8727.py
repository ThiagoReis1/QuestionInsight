from numpy import *
notas = array(eval(input("")))
i = 0

p1 = 3
p2 = 5
p3 = 1

p1 = p1 * notas[0]
p2 = p2 * notas[1]
p3 = p3 * notas[2]

mp = (p1+p2+p3)/(3+5+1)
print(round(mp , 2))
