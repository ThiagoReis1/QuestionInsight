T = 3.50
S = 5.00
a =13.00

variavel = (input("t/s??: "))
q = int(input("quantos t/s?: "))
acais = float(input("quantos?: "))

if variavel == 'T':
	total = (q * T)+(acais*a)
else:
	total = (q * S)+(acais*a)
	
print(total)