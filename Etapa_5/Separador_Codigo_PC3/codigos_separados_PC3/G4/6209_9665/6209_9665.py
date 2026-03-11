N = float(input("digite o numero: "))

cont = 0

while N != -1:
	if N >= 76 and N <= 100:
		cont = cont + 1
	N = float(input("digite o numero: "))
	
print(cont)