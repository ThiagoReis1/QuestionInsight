#UNIVERSIDADE FEDERAL DO AMAZONAS
#ENGENHARIA QUIMICA
#MICHAEL EVANGELISTA DA CRUZ - 21600845

from numpy import *
p = float(input("p: "))
x = array(eval(input("x: ")))
y = array(eval(input("y: ")))

t = p/(p-1)

a = 0

for i in range(size(x)):
	a = a + abs(x[i] + y[i]) ** t
result = (a) ** (1/t)
print(round(result, 5))
