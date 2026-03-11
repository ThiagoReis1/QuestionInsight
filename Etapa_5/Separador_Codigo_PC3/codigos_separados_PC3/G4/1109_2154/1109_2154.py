i = int(input("idade: "))
p = float(input("peso: "))

print("Entradas:", i, "anos e", p, "kg")

if((i >= 12) and (i <= 130) and (p >= 60)):
	print("Dosagem: 1000 mg")
elif((i >= 12) and (i <= 130) and ( p < 60)):
	print("Dosagem: 875 mg")
elif((i < 12) and (p <= 5)):
	print("Dosagem: 75 mg")
elif((i < 12) and (p > 5 or p <=  9)):
	print("Dosagem: 125 mg")
elif((i < 12) and (p >9 or p <= 16)):
	print("Dosagem: 250 mg")
elif((i < 12) and (p >16 or p <= 24)):
	print("Dosagem: 375 mg") 
elif((i < 12) and (p >24 or p <= 30)):
	print("Dosagem: 500 mg")
elif((i < 12) and (p > 30 )):
	print("Dosagem: 750 mg")
else:
	print("Dados invalidos")

