x = float(input("numero real: "))
k = int(input("quantidade de termos: "))
soma = 0
t = 0
a = 1


while t < k:
	soma = soma + x**a/a
	a = a + 2
	t = t + 1
	
print(round(soma, 7))
	