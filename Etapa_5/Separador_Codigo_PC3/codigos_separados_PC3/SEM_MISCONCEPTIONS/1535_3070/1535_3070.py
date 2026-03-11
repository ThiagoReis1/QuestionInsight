x = float(input("numero real: "))
k = int(input("numero inteiro: "))

soma = 0
cont1 = 1
cont2 = 1

while (cont1 <= k):
	soma = soma - ((-1) ** cont1) * ((x ** cont2) / cont2)
	cont1 = cont1 + 1
	cont2 = cont2 + 2
print(round(soma, 6))