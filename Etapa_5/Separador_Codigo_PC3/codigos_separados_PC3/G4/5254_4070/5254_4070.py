p=float(input("Preco: "))
r=int(input("regiao: "))

if r==1:
	v=(p-p*0.4)+p*(10/100)
	print(round(v,2))
elif r==2:
	v=(p-p*0.4)+p*(8/100)
	print(round(v,2))
elif r==3:
	v=(p-p*0.4)
	print(round(v,2))
elif r==4:
	v=(p-p*0.4)+p*(2/100)
	print(round(v,2))
else :
	v='entrada invalida'
	print(v)
	

