from numpy import*
notas = array(eval(input("digite: ")))

i = 0
p1 = 5
p2 = 4
p3 = 3
p4 = 2

p1 = p1 * notas[0]
p2 = p2 * notas[1]
p3 = p3 * notas[2]
p4 = p4 * notas[3]

mp = (p1 + p2 + p3 + p4)/(5+4+3+2)
print(round(mp, 2))
