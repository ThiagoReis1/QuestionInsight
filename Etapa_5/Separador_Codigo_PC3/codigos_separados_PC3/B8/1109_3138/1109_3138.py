idade=int(input(""))
peso=float(input(""))

if(idade>130 or idade<0 or peso<0 or peso>550.0):
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dados invalidos")
	exit()
	
if(idade>=12 and peso>=60):
	dos=1000
elif(idade>=12 and peso<60):
	dos=875
elif(idade<12 and peso<=5):
	dos=75
elif(idade<12 and peso>5 and peso<9):
	dos=125
elif(idade<12 and peso>9 and peso<16):
	dos=250
elif(idade<12 and peso>16 and peso<24):
	dos=375
elif(idade<12 and peso>24 and peso<30):
	dos=500
elif(idade<12 and peso>30):
	dos=750
	
print("Entradas:",idade,"anos e",peso,"kg")
print("Dosagem:",dos,"mg")


