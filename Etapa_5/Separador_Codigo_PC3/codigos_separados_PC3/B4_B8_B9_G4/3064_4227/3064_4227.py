n = input("")
v1 = int(input(""))
v2 = int(input(""))
if (v1>1)and(v1<10)and(v2>1)and(v2<10):
	if (n=="AAMEUL"):
		print(8+(v1+v2))
elif (n=="HETHREDIAH"):
	print(2*(v1+v2))
elif (n=="RAKSHASA"):
	print(10+(v1+v2))
else:
	if(n!="AAUMEL")and(n!="HETHRADIAH")and(n!="RAKSHASA"):
		print("Entrada invalida")
	elif(v1<1)or(v1>10)or(v2<1)or(v2>10):
		print("Entrada invalida")