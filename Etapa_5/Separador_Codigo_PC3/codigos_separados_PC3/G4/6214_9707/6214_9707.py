n = int(input("digite n: "))
cont = 0

while n != -1:
	if n >= 45 and n <= 150:
		cont = cont + 1
	n = int(input("digite n: "))
print(cont)