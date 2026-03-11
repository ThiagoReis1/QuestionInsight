from numpy import*
vetor = array(eval(input("informe as notas: ")))
i = 0

p1 = 3
p2 = 2
p3 = 4
p4 = 1
p5 = 3

p1 = p1 * vetor[0]
p2 = p2 * vetor[1]
p3 = p3 * vetor[2]
p4 = p4 * vetor[3]
p5 = p5 * vetor[4]

mp = (p1+p2+p3+p4+p5)/(3+2+4+1+3)
print(round(mp, 2))