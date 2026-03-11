##Dois numeros pares

n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Terceiro numero:"))

#Condicao#

if (n1 % 2== 0) and (n2 % 2==0):
	print("SIM")
elif (n1 % 2 ==0) and (n3 % 2==0):
	print("SIM")
elif(n2 % 2==0) and (n3 % 2==0):
	print("SIM")
else:
	print("NAO")

	