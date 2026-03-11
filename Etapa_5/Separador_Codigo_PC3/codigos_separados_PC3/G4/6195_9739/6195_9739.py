bacterias = int(input("Insira o numero de bacterias: "))
tx = int(input("qual a taxa de crescimento: "))

i = 0
q = bacterias 

while q < 2 * bacterias:
	q = q + (tx/100) * q
	i = i + 1
print(i)
	