from numpy import*

n = array(eval(input("Digite as notas: ")))
p = [1,2,3]

i = 0
total = 0

total = (n[0]* p[0] + n[1] * p[1] + n[2] * p[2]) / 6

print(round(total,2))