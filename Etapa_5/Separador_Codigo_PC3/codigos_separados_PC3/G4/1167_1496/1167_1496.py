N = int(input("Insira N:"))

i = 1
soma = 0
n =1
d = 1

while (i<=N):
	if (i%2==0):
		soma = soma + ((n**2)/(7+d))
		
	else:
		soma = soma - ((n**2)/(7+d))
	
	i= i+1
	n= n+1
	d= d+2
		
	
	
	
print(round(soma,11))
		