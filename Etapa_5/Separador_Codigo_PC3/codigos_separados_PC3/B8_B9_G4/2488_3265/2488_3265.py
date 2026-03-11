fs = float(input())

print("Entrada: R$", fs)
if (fs > 0):
	if (fs <= 800):
		ns = fs + (fs/100)*50
		print(round("Novo salario: R$", ns), 2)
	elif(fs > 800 and fs <= 1000):
		ns = fs + (fs/100)*40
		print("Novo salario: R$",round(ns, 2))
	elif(fs > 1000 and fs <= 1200):
		ns = fs + (fs/100)*30
		print("Novo salario: R$",round(ns, 2))
	elif(fs > 1200 and fs <= 1400):
		ns = fs + (fs/100)*20
		print("Novo salario: R$",round(ns, 2))
	elif(fs > 1400 and fs <= 1600):
		ns = fs + (fs/100)*10
		print("Novo salario: R$",round(ns, 2))
	elif(fs > 1600):
		ns = fs + (fs/100)*5
		print("Novo salario: R$",round(ns, 2))
else: 
	print("Dado invalido")
	