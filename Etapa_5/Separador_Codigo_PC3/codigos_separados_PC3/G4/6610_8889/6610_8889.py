num = int(input(""))
cont= 1
soma = 0 
while cont <= num:
	if cont%2==0:
		soma = soma + cont 
	cont= cont+1
print("soma=",soma)