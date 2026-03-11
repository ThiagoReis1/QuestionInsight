from numpy import*

dano = array(eval(input(": ")))

a = 0 #posição vetor
cont = 0 #dano
x = 1 # peso ataque

while a < size(dano):
	cont = cont + dano[a] * x
	x = x + 1
	a = a + 1
print(cont)