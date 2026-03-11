n = int(input("Digite o numero: "))

i = n//1000
j = n%1000

k = (i+j)**2

if (k == n):
	diga = "atende"
	
else:
	diga = "nao atende"
	
print(diga)
print(n)