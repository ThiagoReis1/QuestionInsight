X = int(input("Digite a idade: ")) 
Y = float(input("Digite o peso: "))
print("Entradas:",X,"anos e",Y,"kg")

if ( X <= 0) or ( X >=130 ) or ( Y <= 0) or ( Y >= 550):
	print("Dados invalidos")
elif ( X <= 20) and ( Y <= 60):
	print("Grupo de risco: 9")
elif (X >20) and ( X <= 50) and ( Y <= 60):
	print("Grupo de risco: 6")
elif (X >50) and (Y <= 60):
	print("Grupo de risco: 3")
elif (X <= 20) and (Y >60 ) and ( Y<= 90):
	print("Grupo de risco: 8")
elif (X >20) and (X <=50) and (Y >60) and (Y <=90):
	print("Grupo de risco: 5")
elif ( X >50) and (Y >60) and (Y <=90):
	print("Grupo de risco: 2")
elif (X <=20) and (Y>90):
	print("Grupo de risco: 7")
elif ( X>20) and (X <=50) and (Y>90):
	print("Grupo de risco: 4")
elif (X>50) and (Y>90):
	print("Grupo de risco: 1")

	