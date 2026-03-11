num = int(input("Digite um numero: "))

acum = 0

while num >= 0:
	if num>=45 and num<=150:
		acum = acum+1
	num = int(input("Digite um numero: "))
	
print(acum)