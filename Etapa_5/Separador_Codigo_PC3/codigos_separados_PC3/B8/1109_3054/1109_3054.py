idade = int(input("informe a idade: "))
peso = float(input("informe o peso: "))
print("Entradas:", idade,"anos",peso,"kg")

if(idade >= 12) and (peso >= 60):
	print("Dosagem: 1000 mg")
elif(idade >= 12) and (peso < 60):
	print("Dosagem: 875 mg")
elif(idade < 12) and (peso <= 5):
	print("Dosagem: 75 mg")
elif(idade < 12) and (peso > 5) and (peso <= 9):
	print("dosagem: 125 mg")
elif(idade < 12) and (peso > 9) and (peso <= 16):
	print("Dosagem: 250 mg")
elif(idade < 12) and (peso > 16) and (peso <= 30):
	print("Dosagem: 375 mg")
elif(idade < 12) and (peso > 30):
	print("Dosagem: 750 mg")
elif(idade < 0) and (idade > 130) or (peso < 0.0) and (peso > 550.0):
	print("Dados invalidos")
	
	