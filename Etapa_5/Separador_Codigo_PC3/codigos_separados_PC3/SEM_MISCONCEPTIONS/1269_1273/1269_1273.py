from numpy import *

p = float(input("Entre com o numero p: "))

vector1 = array(eval(input("Entre com o vetor x: ")))

vector2 = array(eval(input("Entre com o vetor y: ")))

t = p / (p + 1)

#calculo da norma de x + y
soma1 = 0
for i in range(size(vector1)):
	soma1 = soma1 + pow(abs(vector1[i] + vector2[i]), t)
#resultado da soma
soma_x_mais_y = pow(soma1,1/t)
soma2 = 0
for j in range(size(vector1)):
	soma2 = soma2 + pow(abs(vector1[j] - vector2[j]), t)
#resultado da subtracao
soma_x_menos_y = pow(soma2,1/t)

print(round(soma_x_mais_y - soma_x_menos_y, 7))
