peso=float(input("Peso: "))
idade=int(input("Idade: "))

if ((idade > 12) and (peso >= 60)):
	dose =1000
else:
	dose = 975		
if((idade <12)and(peso==5)):
	dose= 75
	elif((idade<12) and (peso>5) and (peso<=9)):
      dose= 125
   elif((idade<12)and (peso>9) and (peso<=16)):
      dose= 250
   elif((idade<12)and (peso>16) and (peso<=24)):
	   dose= 375
   elif((idade<12) and (peso>24) and (peso<=30)):
	   dose= 500
   elif((idade<12) and peso>30):
	   dose= 750
else(idade>12):
	print("Dados invalidos")
	
print("Entradas: ", idade, "anos", "e", peso, "kg")		
print("Dosagem: ", dose, "mg")