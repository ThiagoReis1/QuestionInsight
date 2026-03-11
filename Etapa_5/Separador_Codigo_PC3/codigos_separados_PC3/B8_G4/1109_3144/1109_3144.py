idd = int(input("idade:"))
peso = float(input("peso:"))

if((0>idd<=130) and (0.0>peso<=550.0)):
	if(idd>12) and (peso>=60):
		print("Entradas:",idd,"anos e",peso,"kg")
		print("Dosagem: 1000 mg")
	elif(idd>12)and (peso<60):
		print("Entradas:",idd,"anos e",peso,"kg")
		print("Dosagem: 875 mg")
	elif(idd<12) and (peso<=5):
		print("Entradas:",idd,"anos e",peso,"kg")
		print("Dosagem: 75 mg")
	elif(idd<12) and (5>peso<=9):
		print("Entradas:",idd,"anos e",peso,"kg")
		print("Dosagem: 125 mg")
	elif(idd<12) and (9>peso<=16):
		print("Entradas:",idd,"anos e",peso,"kg")
		print("Dosagem: 250 mg")
	elif(idd<12) and (16>peso<=24):
		print("Entradas:",idd,"anos e",peso,"kg")
		print("Dosagem: 375 mg")
	elif(idd<12) and (24>peso<=30):
		print("Entradas:",idd,"anos e",peso,"kg")
		print("Dosagem: 500 mg")
	elif((idd<12) and (peso>30)):
		print("Entradas:",idd,"anos e",peso,"kg")
		print("Dosagem: 750 mg")
else:
	print("Entradas:",+idd,"anos e",+peso,"kg")
	print("Dados invalidos")





