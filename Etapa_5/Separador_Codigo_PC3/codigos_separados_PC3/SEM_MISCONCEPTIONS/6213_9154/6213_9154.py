n = int(input())
quantidade = 0
cont = 0
while n != -1:
	if n >= 101 and n <= 201:
		quantidade = quantidade + 1
		cont = cont + 1
	n = int(input())
print(cont)

