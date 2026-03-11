destino = int(input("")) 
idade = int(input(""))

if(destino=="Porto Velho"):
	if(idade<=2):
		valor = 500.00
		passagem = valor * 0
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	elif(3<=idade>=12):
		valor = 500.00
		passagem = valor/2
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	elif(65<=idade):
		valor = 500.00
		passagem = valor*30 / 100
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	else:
		valor = 500.00
		passagem = valor
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
elif(destino == "Santarem"):
   if(idade<=2):
      valor = 370.00
      passagem = valor * 0
      print("Entradas:",destino, idade)
      print("passagem: R$",round(passagem, 2))
   elif(i>=3) and (i<=12):
      valor = 370.00
      passagem = valor/2
      print("Entradas:",destino, idade)
      print("passagem: R$",round(passagem, 2))
   elif(65<=idade):
      valor = 370.00
      passagem = valor*30 / 100
      print("Entradas:",destino, idade)
      print("passagem: R$",round(passagem, 2))
   else:
      valor = 370.00
      passagem = valor
      print("Entradas:",destino, idade)
      print("passagem: R$",round(passagem, 2))
elif(destino == "Belem"):
	if(idade<=2):
		valor = 600.00
		passagem = valor * 0
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	elif(3<=idade>=12):
		valor = 600.00
		passagem = valor/2
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	elif(65<=idade):
		valor = 600.00
		passagem = valor*30 / 100
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	else:
		valor = 600.00
		passagem = valor
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
elif(destino == "Tefe"):
	if(idade<=2):
		valor = 360.00
		passagem = valor * 0
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	elif(3<=idade>=12):
		valor = 360.00
		passagem = valor/2
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	elif(65<=idade):
		valor = 360.00
		passagem = valor*30 / 100
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	else:
		valor = 360.00
		passagem = valor	
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
elif(destino == "Tabatinga"):
	if(idade<=2):
		valor = 550.00
		passagem = valor * 0
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	elif(3<=idade>=12):
		valor = 5500.00
		passagem = valor/2
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	elif(65<=idade):
		valor = 550.00
		passagem = valor*30 / 100
		print("Entradas:",destino, idade)
		print("passagem: R$",round(passagem, 2))
	else:
	   valor = 550.00
	   passagem = valor
print("Entradas:",destino,idade)
print("passagem: R$",round(passagem, 2))

else:
   print("Entradas:", destino, idade)
   print("entradas invalidas")