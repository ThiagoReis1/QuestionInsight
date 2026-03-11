x = int(input("digite: "))

cont = 0

while x != -1:
	if x >= 101 and x <= 201:
		cont = cont + 1
	x = int(input("digite: "))
print(cont)