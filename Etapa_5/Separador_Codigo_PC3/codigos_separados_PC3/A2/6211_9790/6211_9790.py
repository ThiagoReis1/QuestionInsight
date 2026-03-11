valioso = int(input("qual o numero valioso: "))
cont = 0

while valioso != -1:
	if valioso >= 100 and valioso <= 199:
		cont = cont + 1
	else:
		cont = cont
	valioso = int(input("qual o numero valioso: "))
print(cont)
		
	