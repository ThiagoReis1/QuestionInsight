di = float(input())
nm = int(input())
t = 1.2 / 100
soma = di
cont = 0

while (cont < nm):
	cont = cont + 1
	soma = soma + soma * t
	print(round(soma, 2))
	
	