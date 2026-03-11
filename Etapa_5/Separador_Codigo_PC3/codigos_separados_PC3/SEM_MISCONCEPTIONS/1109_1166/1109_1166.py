idade = int(input("qual a idade: "))
peso = float(input("qual o peso: "))
if((idade <0 or idade >130) or (peso <0.0 or peso > 550.0)):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dados invalidos")
if(idade >=12 and idade <=130 and peso >= 60 and peso <=550.0):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem: 1000 mg")
if(idade >=12 and idade <=130 and peso >0.0 and peso <=60):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem: 875 mg")
if(idade >=0 and idade <12 and (peso >=0.0 and peso <= 5)):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem: 75 mg")
if(idade >=0 and idade <12 and (peso >5 and peso <= 9)):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem: 125 mg")
if(idade >=0 and idade <12 and (peso >9 and peso <= 16)):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem: 250 mg")
if(idade >=0 and idade <12 and (peso >16 and peso <= 24)):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem: 375 mg")
if(idade >=0 and idade <12 and (peso >24 and peso <= 30)):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem: 500 mg")
if(idade >=0 and idade <12 and peso >30 and peso <= 500):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem: 750 mg")