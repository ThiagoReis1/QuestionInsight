p = int(input("Digite o prato:"))
s = int(input("Digite a sobremesa:"))
b = int(input("Digite a bebida:"))

print("Entradas:", p,",", s, ",", b)

if (p<1 or p>4) or (s<1 or s>4) or (p<1 or p>4):
	print("Dados invalidos")

else:
	if p==1 :
		tp=180
	elif p==2 :
		tp=230
	elif p==3 :
		tp=250
	elif p==4 :
		tp=350

	if s==1 :
		ts=75
	elif s==2 :
		ts=110
	elif s==3 :
		ts=170
	elif s==4 :
		ts=200

	if b==1 :
		tb=20
	elif b==2 :
		tb=70
	elif b==3 :
		tb=100
	elif b==4 :
		tb=65

	print("Calorias:", (tp + ts + tb) ,"cal")


