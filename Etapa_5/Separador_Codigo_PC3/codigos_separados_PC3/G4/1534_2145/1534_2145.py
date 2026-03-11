x = float(input("Digite um numero: "))
k = int(input("Numero de termos: "))
n = 0
atg = 0
while(n < k):
	atg = atg + ((x ** (2*n + 1))/(2*n + 1))
	n = n + 1
print(round(atg, 7))