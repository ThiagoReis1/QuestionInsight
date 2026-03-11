numero = int(input())
a = numero%3
b = numero%5
if (a==0 and b == 0):
	print("Zuuum")
elif (a==0):
	print("Plunct")
elif (b == 0):
	print ("plact")
else:
	print(numero)

	