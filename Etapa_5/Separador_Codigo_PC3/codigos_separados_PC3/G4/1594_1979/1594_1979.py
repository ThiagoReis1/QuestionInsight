from numpy import*

danos = array(eval(input("Insira o vetor de danos:\n")))

i = 0
p = 1
j = 0
nvet = zeros((size(danos)),dtype = int)

while(i<size(danos)):
	nvet[j] = p * danos[i]
	i = i + 1
	j = j + 1
	p = p + 1
	
dano = sum(nvet)
print(dano)