idade = int(input("qual a idade: "))
peso = float(input("qual o peso: "))
if((idade <0 or idade > 130) or (peso <0 or peso >550)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Dados invalidos")
if((idade >0 and idade <= 20) and (peso >0 and peso <=60)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de risco: 9")
if((idade >20 and idade <= 50) and (peso >0 and peso <=60)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de risco: 6")
if((idade >50) and (peso >0 and peso <=60)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de risco:  3")
if((idade >0 and idade <= 20) and (peso >60 and peso <=90)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de risco: 8")
if((idade >20 and idade <= 50) and (peso >60 and peso <=90)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de risco: 5")
if((idade >50) and (peso >60 and peso <=90)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de risco: 2")
if((idade >0 and idade <= 20) and (peso >90)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de risco: 7")
if((idade >20 and idade <= 50) and (peso>90)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de risco: 4")
if((idade >50) and (peso >90)):
	print("Entradas: ",idade,"anos e",peso,"kg")
	print("Grupo de riso: 1")



	