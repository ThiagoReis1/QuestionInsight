n = int(input("Numero do movimento: "))
s = 0
while (n != 0):
	s = s + n
	n = int(input("Numero do movimento: "))
	
if (s == 0):
	print(s)
	print("Inicial")
elif (s > 0):
	print(s)
	print("Direita")
else:
	print(s)
	print("Esquerda1")

