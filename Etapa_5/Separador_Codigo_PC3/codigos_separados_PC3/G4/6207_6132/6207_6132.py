n = int(input("digite um numero: "))
cont = 0

while(n>0):
	if(n>=26) and (n<=50):
		cont = cont + 1
	n = int(input("digite um numero: "))
print(cont)