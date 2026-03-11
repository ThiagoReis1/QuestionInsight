num = int(input("numeros:"))

cont = 0

while num != -1:
	if num >= 100 and num <= 199:
		cont = cont + 1
	num = int(input("numeros:"))
print(cont)