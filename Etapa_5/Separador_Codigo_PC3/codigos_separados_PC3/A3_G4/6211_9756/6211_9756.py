num = int(input("Informe o numero: "))
cont = 0
soma  = 0

while num != -1:
	if num >= 100 and num <= 199:
		cont = cont +1
	num = int(input("Informe o numero: "))
		
print (cont)