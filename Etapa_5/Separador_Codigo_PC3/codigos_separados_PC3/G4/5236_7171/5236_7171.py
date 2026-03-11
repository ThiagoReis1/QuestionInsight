n=int(input("Digite um numero:"))

if (n>=1):
	if (n%3==0) and (n%5==0):
		print("PirlimPimpim")
	elif (n%5==0):
		print(Pimpim)
	elif (n%3==0):
		print ("Pirlim")
	else:
		print (n)
		