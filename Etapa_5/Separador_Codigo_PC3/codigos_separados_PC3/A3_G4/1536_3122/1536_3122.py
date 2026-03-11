x = float(input("x: "))
k = int(input("k: "))

cont = 1
z = 0
soma = 0

while (cont <= k):
	z = - (-1) ** cont * (x ** cont) /  cont
	soma = soma + z
	cont = cont + 1

print(round(soma, 10))