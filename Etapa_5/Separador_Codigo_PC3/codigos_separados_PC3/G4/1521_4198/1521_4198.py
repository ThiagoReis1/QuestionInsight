n= int(input("Digite a capacidade do navio: "))
e= int(input("Digite a quantidade de estoque inicial: "))
q= int(input("Digite a quantidade que chega no deposio: "))
a= 0
c= 1
while(n>=e):
	e= e+q-n
	a= a + 1
	c= c + 1
print(c)
