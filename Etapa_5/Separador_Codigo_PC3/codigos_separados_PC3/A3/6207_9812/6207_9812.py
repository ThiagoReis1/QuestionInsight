n = int(input('numero: '))

cont = 0 
total_n = 0

while (n != -1):
	if 26 <= n <= 50:
		cont += 1
	n = int(input('numero: '))
print(cont)