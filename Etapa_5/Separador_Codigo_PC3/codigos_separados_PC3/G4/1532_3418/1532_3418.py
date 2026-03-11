from math import*

soma = 0
i = 0

x = float(input("Numero x: "))
k = int(input("Numero k: "))

while(i<k):
	soma = soma + (x)**(2*i+1)/(factorial(2*i+1))
	i=i+1
	
print(round(soma, 9))
	
