idade = float(input())
peso = float(input())

if (idade<=0 or idade>=130 or peso<=0.0 or peso>=550):
	print ("Dados invalidos")
elif (idade<=20 and peso<=60):
	print ("Grupo de risco: 9")
elif (idade>20 or idade<=50) and (peso<=60):
	print ("Grupo de risco: 6")
elif (idade >50 and peso<=60):
	print ("Grupo de risco: 3")
elif (idade<=20) and (peso>60 or peso<=90):
	print ("Grupo de risco: 8")
elif (idade<20 or idade<=50) and (peso>60 or peso<=90):
	print ("Grupo de risco: 5")
elif (idade>50) and (peso<60 or peso<=90):
	print ("Grupo de risco: 2")
elif (idade<=20 and peso>90):
	print ("Grupo de risco: 7")
elif (idade<20 or idade<=50) and (peso>90):
	print ("Grupo de risco: 4")
elif (idade>50 and peso>90):
	print("Grupo de risco: 1")