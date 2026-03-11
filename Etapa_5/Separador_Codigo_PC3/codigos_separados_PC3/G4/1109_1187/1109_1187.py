idd = int(input("Digite a idade:"))
peso = float(input("Digite o peso:"))
if((idd <0 or idd > 130) or (peso <0.0 or peso > 550.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dados invalidos.")
if(idd >=12 and idd <=130 and (peso>=60 and peso <=550.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dosagem: 1000 mg")
if(idd >=12 and idd <=130 and (peso>=0.0 and peso <60.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dosagem: 875 mg")
if(idd >=0 and idd <12 and (peso >=0.0 and peso <=5.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dosagem: 75 mg")
if(idd >=0 and idd <12 and (peso >5.0 and peso <=9.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dosagem: 125 mg")
if(idd >=0 and idd <12 and (peso >9.0 and peso <=16.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dosagem: 250 mg")
if(idd >=0 and idd <12 and (peso >16.0 and peso <=24.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dosagem: 375 mg")
if(idd >=0 and idd <12 and (peso >24.0 and peso <=30.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dosagem: 500 mg")
if(idd >=0 and idd <12 and (peso >30.0)):
	print("Entradas:",idd,"anos e",peso,"kg")
	print("Dosagem: 750 mg")

	

	