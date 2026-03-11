from numpy import *
notas = array(eval(input("informe as notas: ")))
i = 0

p1 = 2
p2 = 1
p3 = 5

p1 = p1 * notas[0]
p2 = p2 * notas[1]
p3 = p3 * notas[-1]

mp = (p1+p2+p3)/(2+1+5)
print(round(mp, 2))