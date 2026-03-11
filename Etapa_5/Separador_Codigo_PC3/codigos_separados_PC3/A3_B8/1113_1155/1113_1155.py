idade=int(input("digite o idade"))
peso=float(input("digite o peso"))
#idade menor que 20 anos
if(idade <= 20) and (peso <= 60):
    grupo="9"
elif(idade <= 20) and (60 < peso <= 90):
	grupo="8"
elif(idade <= 20) and (peso > 90):
 	grupo="7"
if(20 < idade <= 50) and (peso <= 60):
	grupo="6"
elif(20 < idade <= 50) and (60 < peso <= 90):
	grupo="5"
elif(20 < idade <= 50) and (peso > 90):
	grupo="4"
if(idade > 50) and (peso <= 60):
  	grupo="3"
elif(idade > 50) and (60 < peso <= 90):
	grupo="2"
elif(idade > 50) and (peso > 90):
	grupo="1"
print("Entradas:",idade,"anos","e",peso,"kg")
if(0<idade<=130)and(0<peso<=550):
	print("Grupo de risco:",grupo)
else:
	print("Dados invalidos")