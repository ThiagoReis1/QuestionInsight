idade = int(input("insira a idade: "))
pais = input().upper()
v = 2023 - idade
if pais == 'B':
	if v >= 21:
		print("sim")
		print(v - 21)
	else:
		print ("nao")
		print (21 - v)
elif pais == 'J':
	if v >= 20:
		print("sim")
		print(v - 20)
	else:
		print("nao")
		print(20-v)
else: 
	print("invalido")
	
	