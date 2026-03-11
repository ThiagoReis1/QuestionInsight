num = int(input("numeros: "))
cont = 0
while(num>=0):
	if(num>=26 and num<=85):
		cont+= 1
	num = int(input("numeros: "))
print(cont)