n = int(input("numero inteiro: "))

if(n>=1 and n%3 == 0 and n%5 == 0):
	print("Zuuum")
else:
	if(n>=1 and n%3 == 0):
		print("Plunct")
	elif(n>=1 and n%5 == 0):
		print("Plact")	
	else:
		print(n)
	
	
