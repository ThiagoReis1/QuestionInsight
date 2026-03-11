p = float(input("preco de custo: "))

if (p<=50):
	x = p
	y = p+x
elif (p>=50.01) and (p<=100):
	x = p*0.50
	y = p+x
elif (p>=100.01) and (p<=500):
	x = p*0.40
	y  =p+x
elif (p>500):
	x = p*0.30
	y = p+x

print(round(y,2))