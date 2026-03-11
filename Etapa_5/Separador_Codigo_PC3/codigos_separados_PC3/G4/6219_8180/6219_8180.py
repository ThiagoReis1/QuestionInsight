x = int(input(": "))
y = int(input(": "))
soma=x+y
cont = 0
while(x < y):
	soma = soma + 1
	if(soma%3 == 0):
		cont = cont + 1
	
print(cont)