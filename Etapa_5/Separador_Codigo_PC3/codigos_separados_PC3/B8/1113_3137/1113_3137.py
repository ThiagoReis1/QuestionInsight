idade = int(input("idade: "))
peso= float(input("peso: "))

if (idade>130) or (peso>550.0):
	y="Dados invalidos"
	print(y)
elif(idade>50) and (peso>90):
	y="1"
	print("Grupo de risco:", y)
elif (idade>50) and (60<peso<90):
	y="2"
	print("Grupo de risco:", y)
elif (idade>50) and (peso<60):
	y="3"
	print("Grupo de risco:", y)
elif (20<idade<50) and (peso>90):
	y="4"
	print("Grupo de risco:", y)
elif (20<idade<50) and (60<peso<90):
	y="5"
	print("Grupo de risco:", y)
elif (20<idade<50) and (peso<60):
	y="6"
	print("Grupo de risco:", y)
elif (idade<20) and (peso>90):
	y="7"
	print("Grupo de risco:", y)
elif (idade<20) and (60<peso<90):
	y="8"
	print("Grupo de risco:", y)
elif (idade<20) and ( peso<60):
	y="9"
	print("Grupo de risco:", y)
print("Entradas:",idade,"anos","e",peso,"kg")
	