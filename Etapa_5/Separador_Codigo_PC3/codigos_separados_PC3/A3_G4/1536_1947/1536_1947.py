n = 1
x = float(input("Valor real x:"))
k = int(input("Coloque k termos a serem contados:"))
ln=0
valor = 1
log=0
while n <= k:
	log= (x ** (n))/(n)
	ln = ln + (valor * log)
	valor = - valor
	n = n + 1
print(round(ln, 10))