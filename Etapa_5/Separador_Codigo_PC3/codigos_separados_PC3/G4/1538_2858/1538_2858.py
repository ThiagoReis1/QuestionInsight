x = float(input("Digite um numero real: "))
k = int(input("Digite um numero inteiro k:"))
cont = 0
z = 2
v = (x**z)
total = 0
while(cont <= k):
	total = total + (v * -1)
	cont = cont + 1
	z = z + 2
	v = v * -1
	print(total)
total = 1 - total 
print(round(total, 8))