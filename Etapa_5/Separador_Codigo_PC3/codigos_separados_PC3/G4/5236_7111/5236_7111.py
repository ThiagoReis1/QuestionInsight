N= int (input("Digite um numero inteiro:"))

if (N>=1) and (N%3==0) and (N%5==0):
	print("PirlimPimpim")
elif (N>=1) and (N%3==0):
	print("Pirlim")
elif (N>=1)and (N%5==0):
	print ("Pimpim")
else:
	print(N)