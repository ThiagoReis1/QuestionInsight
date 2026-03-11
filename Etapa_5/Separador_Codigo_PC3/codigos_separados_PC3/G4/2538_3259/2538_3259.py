s = int(input("Digite o valor do sitio: "))
di = int(input("Digite o valor inicial do deposito: "))
m = int(input("Digite o valor mensal do deposito: "))
j = float(input("Digite a taxa de juros: "))

t = 0
d = di

if (s>0) and (d>0) and (m>0) and(j>0):
	while ( s>d):
	
		vm = m + ((m * j)/ 100)
		d = round(d + vm , 2)
		t = t + 1
	print(t)	
else: 
	print("Dados incorretos")
