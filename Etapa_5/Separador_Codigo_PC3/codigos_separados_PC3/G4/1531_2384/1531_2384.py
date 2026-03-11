from math import*

x = eval(input("Insira o ângulo em radianos: "))
k = int(input("Qual a quantidade de termos da série?"))
n = 0
a = 2
cos = 1

if(k == 1):
	print(cos)
else:
	while(n<(k-1)):
		if(n%2==0):
			cos = cos - ((x)**(a))/factorial(a)
			n = n + 1
			a = a + 2
			
		else:
			cos = cos + ((x)**(a))/factorial(a)
			a = a + 2
			n = n + 1
	print(round(cos,10))