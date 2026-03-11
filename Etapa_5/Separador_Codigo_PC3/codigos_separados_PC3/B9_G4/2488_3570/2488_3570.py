at = float(input("salario atual:"))

print("Entrada: R$",at)
if (at >= 0):
	if (at <= 800):
		nv = at + (at*0.5)
	elif ( at > 800) and (at <= 1000):
		nv = at + (at*0.4)
	elif (at > 1000) and (at <= 1200):
		nv = at + (at*0.3)
	elif (at > 1200) and (at <= 1400):
		nv = at + (at*0.2)
	elif (at > 1400) and (at <= 1600):
		nv = at + (at*0.1)
	else:
		nv = at + (at*0.05)
	print("Novo salario: R$",round(nv,2))	
else:
	print("Dado invalido")