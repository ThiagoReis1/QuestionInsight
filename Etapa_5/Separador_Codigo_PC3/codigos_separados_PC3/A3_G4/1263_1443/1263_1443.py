from numpy import *

p = float(input("Digite o valor de p: "))
x = array(eval(input("Digite o vetor x: ")))
y = array(eval(input("Digite o vetor y: ")))
z = array(zeros(size(x)))
t = p / (p + 1)
i = 0
while(i < size(x)):
	if(size(x) == size(y)):
		z[i] = abs(2 * x[i] + 3 * y[i])
		i = i + 1
	else:
		mens = "Erro"
j = 0
cont = 0
while(j < size(z)):	
	cont = (cont + (abs(z[i]) ** t)) ** (1 / t)
	j = j + 1
	i = i + 1
	
print(round(cont, 7))	