num = int(input("numero: "))
cont = 0

while(num >= 0):
	if(num>=26 and num<=50):
		cont = cont + 1
	num = int(input("numero: "))
print(cont)