X = int(input("digite o valor de X: "))
Y = int(input("digite o valor de Y: "))

soma_dos_divisiveis= 0
 
for num in range(X,Y + 1):
	if num % 3 == 0:
		soma_dos_divisiveis += num
print(soma_dos_divisiveis)