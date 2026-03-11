p = float(input('digite um valor:'))
if(p>0)and(p<=50)or(p>=50.01)and(p<=100)or(p>=100.01)and(p<=500)or(p>500):
	if(p>0)and(p<=50):
		l = p+p
		print(round(l,2))
	elif(p>=50.01)and(p<=100):
		l = (p*0.50)+p
		print(round(l,2))
	elif(p>=100.01)and(p<=500):
		l = ((p*40)/100)+p
		print(round(l,2))
	elif(p>500):
		l = ((p*30)/100)+p
		print(round(l,2))
else:
	print('valor invalido')