n = int(input("digite n:"))
cont = 0

while n != -1:
	if n >= 101 and n <= 201:
		cont = cont + 1
	n = int(input("digite n: "))
print(cont)