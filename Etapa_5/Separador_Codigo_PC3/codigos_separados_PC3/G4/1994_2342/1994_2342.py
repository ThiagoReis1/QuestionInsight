nome=input().lower()

if(nome=="histinida"):
	print(round(6*12.011 + 10*1.0079 + 3*14.00674 + 2*15.9994,2))
elif(nome=="leucina"):
	print(round(6*12.011 + 13*1.0079 + 14.00674 + 2*15.99994,2))
elif(nome=="lisina"):
	print(round(6*12.011 + 15*1.0079 + 2*14.00674 + 2*15.99994,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")
	