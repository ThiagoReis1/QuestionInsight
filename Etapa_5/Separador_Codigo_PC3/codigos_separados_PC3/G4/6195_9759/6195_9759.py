a = int(input("Informe o numero de bacterias: "))
b = float(input("Informe a taxa de crescimento: "))

i = 0
q = a 
while q < 2*a:
	q = q + (b/100) * q 
	i = i + 1
print(i)
	