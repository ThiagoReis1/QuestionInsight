a=int(input("Age:"))
p=float(input("peso:"))
print("Entradas:",a,"anos e",p,"kg")
if((a>=0 and a<=130) and (p>0.0 and p<=550.0)):
	if(a>=12): 
		if(p>=60):
			print("Dosagem: 1000 mg")
		else:
			print("Dosagem: 875 mg")
	elif(a<12):
		if(p<=5):
			print("Dosagem: 75 mg")
		elif(p>5 and p<=9):
			print("Dosagem: 125 mg ")
		elif(p>9 and p<=16):
			print("Dosagem: 250 mg ")
		elif(p>16 and p<=24):
			print("Dosagem: 375 mg")
		elif(p>24 and p<=30):
			print("Dosagem: 500 mg")
		else:
			print("Dosagem: 750 mg ")
else:
	print("Dados invalidos")