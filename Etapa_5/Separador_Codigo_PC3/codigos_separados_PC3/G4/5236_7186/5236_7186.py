from math import*

N= int(input("Digite um numero: "))

if(N >= 1):
	if(N%3 == 0 and N%5 == 0):
		print("PirlimPimpim")
	elif(N%3 == 0):
		print("Pirlim")
	elif(N%5 == 0):
		print("Pimpim")
	else:
		print(N)