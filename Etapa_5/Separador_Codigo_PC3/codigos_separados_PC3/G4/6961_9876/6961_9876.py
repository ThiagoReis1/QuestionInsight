x = int(input("insira o valor de 'x': "))
y = int(input("insira o valor de 'y': "))

i = x
cont = 0 

while i <= y:
	if i % 3 == 0:
		cont += i
	i += 1
print(cont)