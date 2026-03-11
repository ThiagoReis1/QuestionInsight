iden = int(input())
peso = float(input())
print("Entradas:",iden,"anos e",round(peso,1),"kg")
if iden>0 and iden<130 and peso>0 and peso<=550:
	if peso<=60 and iden<=20:
		print("Grupo de risco: 9")
	elif peso<=60 and iden>20 and iden<=50:
			print("Grupo de risco: 6")
	elif peso<=60 and iden>50:
			print("Grupo de risco: 3")
	elif peso>60 and peso<=90 and iden<=20:
			print("Grupo de risco: 8")
	elif peso>60 and peso<=90 and iden>20 and iden<=50:
			print("Grupo de risco: 5")
	elif peso>60 and peso<=90 and iden>50:
			print("Grupo de risco:2")
	elif peso>90 and iden<=20:
			print("Grupo de risco: 7")
	elif peso>90 and iden>20 and iden<=50:
			print("Grupo de risco: 4")
	elif peso>90 and iden>50:
			print("Grupo de risco: 1")
else:
	print("Dados invalidos")