N=input("nome")
A=(a).lower()
if(A=="GLUTAMINA"):
	v=(12.011*5)+(1.00794*8)+(14.0067)+(15.9994*4)
	print (round(v,2))
elif(A=="SERINA"):
	v=(12.011*3)+(1.00794*7)+(14.0067)+(15.9994*3)
	print(round (v , 2))
elif(A=="TREONINA"):
	v=(12.011*4)+(1.00794*9)+(14.0067)+(15.9994*3)
	print(round (v , 2))
else:
	print("Entrada:",a)
	print("Dado Invalido")