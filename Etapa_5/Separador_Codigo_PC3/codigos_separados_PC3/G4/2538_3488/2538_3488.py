S = float(input("valor: "))
D = float(input("valor1: "))
M = float(input("valor3: "))
j = float(input("va4: "))

soma = 0
t = 0

while(S > 0 and D>0 and M>0 and j>0):
	if(S > D):
		soma = soma + (D + M * j)
		soma = round(soma, 2)
		t = t + 1
		print(soma)

else:
	print("Dados incorretos")