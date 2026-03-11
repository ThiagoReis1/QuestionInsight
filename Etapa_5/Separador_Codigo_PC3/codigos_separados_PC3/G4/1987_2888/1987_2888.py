nome = input().upper()

if(nome=="ALANINA"):
	op1 = (15.9994*2)+(12.011*3)+(14.00674)+(1.00794*7)
	print(round(op1,2))
elif(nome=="VALINA"):
	op2 = (15.9994*2)+(12.011*5)+(14.00674)+(1.00794*11)
	print(round(op2,2))
elif(nome=="TIROSINA"):
	op3 = (15.9994*3)+(12.011*9)+(14.00674)+(1.00794*11)
	print(round(op3,2))
else:
	print("Entrada:", nome)
	print("Dado Invalido")
