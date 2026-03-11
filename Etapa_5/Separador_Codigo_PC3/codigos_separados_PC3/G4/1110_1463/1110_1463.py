#Ingrid do Nascimento Mendes
#14/07/2016

#prato, sobremesa e bebida
p = int(input())
s = int(input())
b = int(input())
total = 0

print ("Entradas:", p, ",", s, ",", b)

if (p==1 or p==2 or p==3 or p==4) and (s==1 or s==2 or s==3 or s==4) and (b==1 or b==2 or b==3 or b==4):
	if (p==1):
		total = total + 180
	elif (p==2):
		total = total + 230
	elif (p==3):
		total = total + 250
	else:
		total = total + 350
	if (s==1):
		total = total + 75
	elif (s==2):
		total = total + 110
	elif (s==3):
		total = total + 170
	else:
		total = total + 200
	if (b==1):
		total = total + 20
	elif (b==2):
		total = total + 70
	elif (b==3):
		total = total + 100
	else:
		total = total + 65
	print ("Calorias:", total, "cal")
else:
	print ("Dados invalidos")