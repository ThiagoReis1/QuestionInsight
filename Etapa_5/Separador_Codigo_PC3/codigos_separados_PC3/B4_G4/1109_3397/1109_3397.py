i = int(input("Entradas: "))
p = float(input("peso: "))
print("Entradas:",i,"anos","e", p,"kg")
if(i < 0) and (p < 0):
		print("Dados invalido")
elif(i > 130) and (p > 550.0): 
		print("Dados invalidos")
elif(i >= 12) and (p >= 60):
		print("Dosagem: 1000 mg")
elif(i >= 12) and (p < 60):
		print("Dosagem: 875 mg")
elif(i < 12) and (p <= 5):
		print("Dosagem: 75 mg")
elif(i < 12) and (p > 5) and (p <= 9):
		print("Dosagem: 125 mg")
elif(i < 12) and (p > 9) and (p <= 16):
		print("Dosagem: 250 mg")
elif(i < 12) and (p > 16) and (p <= 24):
		print("Dosagem: 375 mg")
elif(i < 12) and (p > 24) and (p <= 30):
		print("Dosagem: 500 mg")
elif(i < 12) and (p > 30) and (p <= 59):
		print("Dosagem: 750 mg")
else:
		print("Dados invalidos")