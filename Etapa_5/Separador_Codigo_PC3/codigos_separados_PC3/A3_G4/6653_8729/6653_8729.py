from numpy import*
n = array(eval(input("Informe as notas: ")))
i = 0

p1 = 3
p2 = 5
p3 = 1

p1 = p1*n[0]
p2 = p2*n[1]
p3 = p3*n[-1]

mf = (p1+p2+p3)/(5+1+3)
print(round(mf,2))