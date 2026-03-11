n = int(input("numero:"))
cont = 0
while n != -1:
	if n >= 26 and n <= 50:
		cont = cont+ 1
	n = int(input("numero:"))
print(cont)