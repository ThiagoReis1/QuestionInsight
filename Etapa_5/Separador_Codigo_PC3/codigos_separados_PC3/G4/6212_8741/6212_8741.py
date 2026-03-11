n = int(input("qual o indice: "))
cont = 0

while n != -1:
	if n >= 26 and n <= 85:
		cont = cont + 1
	n = int(input("qual o indice: "))
		
print(cont)
	