o = input("digite T se for tapioca ou S se for salgado (T/S): ").upper()
q = int(input("digite a qtd de tapioca e salgado: "))
qacai = int(input("digite a qtd de acai: "))

t = 3.50
s = 5.00
a = 13.00

if(o == "T"):
	m = (q * t) + (qacai * a)
	print(round(m, 2))
else:
	m = (q * s) + (qacai * a)
	print(round(m, 2))