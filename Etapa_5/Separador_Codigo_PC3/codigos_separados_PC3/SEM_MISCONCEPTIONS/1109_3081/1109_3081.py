idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso: "))
print("Entradas:",idade,"anos e",peso,"kg")
if(idade>=0 and idade<12 and peso>=0 and peso<=5 ):
	print("Dosagem: 75 mg")
elif(idade>=0 and idade<12 and peso>5 and peso<=9):
	print("Dosagem: 125 mg")
elif(idade>=0 and idade<12 and peso>9 and peso<=16):
	print("Dosagem: 250 mg")
elif(idade>=0 and idade<12 and peso>16 and peso<=24):
	print("Dosagem: 375 mg")
elif(idade>=0 and idade<12 and peso>24 and peso<=30):
	print("Dosagem: 500 mg")
elif(idade>=0 and idade<12 and peso>30):
	print("Dosagem: 750 mg")
elif(idade>=12 and idade<=130 and peso>=60 and peso<=550):
	print("Dosagem: 1000 mg")
elif(idade>=12 and idade<=130 and peso<60):
	print("Dosagem: 875 mg")
else:
	print("Dados invalidos")