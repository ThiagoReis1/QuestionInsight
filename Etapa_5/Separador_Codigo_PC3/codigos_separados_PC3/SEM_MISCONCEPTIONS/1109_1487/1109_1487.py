idade = int(input("digite a idade: "))
peso = float(input("digite o peso: "))
if(idade>=12)and(peso>=60):
	men = "1000 mg"
	print("Entradas:",idade," anos e",peso,"kg")
	print("Dosagem:",men,"mg")	
	if(peso<60):
		men = "875 mg"
	
	
	
	
	
	
	
	
	
	
	
else:
	print("Entradas:",idade,"e",peso,"kg")
	print("Dados invalidos")