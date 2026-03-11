n = int(input("digite um numero:"))

cont = 0

while n != -1:
	if n >= 76 and n <= 100:
		cont = cont + 1
	n = int(input("digite um numero:"))
print(cont)