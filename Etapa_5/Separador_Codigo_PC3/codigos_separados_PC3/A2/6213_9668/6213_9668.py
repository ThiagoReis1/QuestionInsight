numero= int(input("numero: "))

num= 0

while( numero != -1 ):
	if numero <= 201 and numero >= 101:
		num = num + 1
		numero = int(input("numero: "))
	else:
		num = num
		numero = int(input("numero: "))
		
print (num)