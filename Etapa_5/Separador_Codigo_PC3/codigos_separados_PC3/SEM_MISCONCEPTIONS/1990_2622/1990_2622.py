amino = input().upper()

if(amino == "GLUTAMINA"):
	x = 12.011*5 + 1.00794*8 + 14.0067 + 15.9994*4
	print(round(x,2))
elif(amino == "SERINA"):
	x = 12.011*3 + 1.00794*7 + 14.0067 + 15.9994*3
	print(round(x,2))
elif(amino == "TREONINA"):
	x = 12.011*4 + 1.00794*9 + 14.0067 + 15.9994*3
	print(round(x,2))
else:
	print("Entrada:",amino)
	print("Dado Invalido")