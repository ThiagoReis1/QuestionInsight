n =float(input("Digite um numero inteiro: "))
tres =n%3
cinco = n%5

if(n >= 1):
	if(tres==0 and cinco != 0):
		print("Auau")
	elif(cinco==0 and tres != 0):
		print("Miau")
	elif(tres==0 and cinco==0):
		print("AuauMiau")
	else:
		print(n)