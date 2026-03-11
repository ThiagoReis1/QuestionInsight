from numpy import *
notas = array(eval(input("informe as notas: ")))

i = 0

p1 = 3
p2 = 4
p3 = 2
p4 = 1
p5 = 4
p6 = 5

p1 = p1* notas[0]
p2 = p2* notas[1]
p3 = p3* notas[2]
p4 = p4* notas[3]
p5 = p5* notas[4]
p6 = p6* notas[5]

mp = (p1+p2+p3+p4+p5+p6)/(3+4+2+1+4+5)
print(round(mp, 2))