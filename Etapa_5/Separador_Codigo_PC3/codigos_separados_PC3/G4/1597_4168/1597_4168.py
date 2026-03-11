from numpy import*
c = array(eval(input("itens comprados:")))
x = 5
y = 80
i = 0
soma = sum(c)

while((i > 0) and (c[i] > y)):
	if(c[i] > y):
		custo = soma + x
		print(round(custo,2))
	i = i + 1
	
print(round(soma, 2))