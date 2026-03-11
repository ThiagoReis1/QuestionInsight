mole=input("Nome da molecula: ")
x=mole.lower()
if(x=="histidina" or x=="leucina" or x=="lisina"):
	if(x=="histidina"):
		c=6
		h=10
		n=3
		o=2
		pm=12.011*c + 1.0079*h + 14.00674*n + 15.9994*o
		print(round(pm,2))
	elif(x=="leucina"):
		c=6
		h=13
		n=1
		o=2
		pm=12.011*c + 1.0079*h + 14.00674*n + 15.9994*o
		print(round(pm,2))
	elif(x=="lisina"):
		c=6
		h=15
		n=2
		o=2
		pm=12.011*c + 1.0079*h + 14.00674*n + 15.9994*o
		print(round(pm,2))
else:
	print("Entrada: ", x)
	print("Dado Invalido")
		