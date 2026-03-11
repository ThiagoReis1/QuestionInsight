from numpy import*

quant = array(eval(input("Digite a quantidade de alunos:")))
c = 0

for i in range(size(quant)):
	if(quant[i] % 2 != 0):
		c = c + 1
print(c)

valor = zeros(c, dtype = int)
cont = 0 
j = 0
for j in range(size(quant)):
		if(quant[j] % 2 != 0):
			valor[cont] = j
			cont = cont + 1
print(valor)