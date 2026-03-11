a = int(input("Digite o numero de bacterias: "))
b = int(input("digite a porcetagem da taxa de crecimento: "))

i = 0 
q = a
while q < 2*a:
	q = q + (b/100)* q
	i = i + 1
print(i)	