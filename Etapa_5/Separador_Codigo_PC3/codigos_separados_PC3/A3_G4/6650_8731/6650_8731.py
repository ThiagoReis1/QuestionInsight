from numpy import*
notas = array(eval(input("informe as notas: ")))
i = 0 

p1 = 4
p2 = 3

p1 = p1* notas[0]
p2 = p2* notas[1]

mp = (p1+p2)/(4+3)
print(round(mp, 2))