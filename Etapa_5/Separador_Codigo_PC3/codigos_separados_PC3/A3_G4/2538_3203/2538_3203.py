s = float(input("Valor do sitio: "))
d = float(input("Valor inicial: "))
m = float(input("Deposito mensal: "))
j = float(input("Taxa de juros: "))

t = 0
cont = 0
if s>0 and d>0 and m>0 and j>0 :
	while d<s:
		d = d + (d*(j/100)) + m
		d = round(d,2)
		t = t+ 1
	print(t)
else:
	print("Dados incorretos")
