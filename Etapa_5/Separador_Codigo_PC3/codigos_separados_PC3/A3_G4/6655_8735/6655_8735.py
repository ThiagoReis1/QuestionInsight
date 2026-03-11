from numpy import *

notas = array(eval(input("informe as notas: ")))

i = 0

p1 = 5
p2 = 1

p1 = p1 * notas[0]
p2 = p2 * notas[1]
mp = (p1+p2)/ (5+1)
print(round(mp, 2))
	
