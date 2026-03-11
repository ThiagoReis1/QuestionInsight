a=input("Nome:")


if(a.upper()=="ALANINA"):
	peso=12.011*3 +1.00794*7 +14.00674+15.9994*2
	print(round(peso,2))
elif(a.upper()=="VALINA"):
	peso=12.011*5 +1.00794*11 +14.00674+15.9994*2
	print(round(peso,2))
elif(a.upper()=="TIROSINA"):
	peso=12.011*9 +1.00794*11 +14.00674+15.9994*3
	print(round(peso,2))
else:
	print("Entrada:",a)
	print("Dado Invalido")
	