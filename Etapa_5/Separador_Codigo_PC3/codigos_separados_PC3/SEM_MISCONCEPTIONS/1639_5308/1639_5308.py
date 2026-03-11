from numpy import*

quant = array(eval(input("quantidade de alunos: ")))

c = 0

d = 0

for i in range(size(quant)):
	if quant[i] % 2 == 0:
		c = c + 1
		
saida = zeros(c,dtype=int)

for i in range(size(quant)):
	if quant[i] % 2 == 0:
		saida[d] = i
		d = d + 1
print(c)
print(saida)