# faça seu código aqui!
cont = 1
acm = 0

num = int(input("Digite o numero: "))

if(cont <= num):
	while(cont <= num):
		res = cont**3
		acm = acm + res
		cont = cont + 1
		
print("soma= ", acm)