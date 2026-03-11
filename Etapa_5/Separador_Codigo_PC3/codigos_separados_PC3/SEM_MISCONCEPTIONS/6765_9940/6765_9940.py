ano= int(input(" "))
pais= input(" ").upper()

idade= 2023-ano
if pais=="B":
	falta= 18-idade
	if idade>=18:
		print("sim")
		print(falta)
	else:
		print("nao")
		print(falta)
elif pais=="R":
	falta= 21-idade
	if idade>=21:
		print("sim")
		print(falta)
else:
	print("invalido")