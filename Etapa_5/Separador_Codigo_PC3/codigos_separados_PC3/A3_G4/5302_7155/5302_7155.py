x = float(input("Quantidade inicial da massa: "))
n  = float(input("Qualditade de anos : "))

cont = 0
soma = x

while (cont < n):
	soma = soma - (soma * (5/100))
	cont = cont + 1
	s = soma
	print(round(soma,2))