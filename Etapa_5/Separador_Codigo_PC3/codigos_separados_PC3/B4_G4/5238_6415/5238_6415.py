a = int(input("Digite um numero inteiro:"))
b = int(input("Digite um numero inteiro:"))
c = int(input("Digite um numero inteiro:"))

if(a and b >= 1000):
	print("SIM")

elif(a and c >= 1000):
	print("SIM")

elif(c and b >= 1000):
	print("SIM")

else:
	print("NAO")