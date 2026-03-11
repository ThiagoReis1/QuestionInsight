p = int(input())
s = int(input())
b = int(input())
total =0

if (p<1 or p>4 or s<1 or s>4 or b<1 or b>4):
	print ("Entradas", p, ",", s, ",", b)
	print ("Dados invalidos")
else:
	if(p==1):
		x=180
		total = x
	elif (p==2):
		x=230
		total = x
	elif (p==3):
		x=250
		total = x
	elif(p==4):
		x=350
		total = x
	elif(s==1):
		y=75
		total = x + y
	elif (s==2):
		y=110
		total = x + y
	elif (s==3):
		y=170
		total = x + y
	elif(s==4):
		y=200
		total = x + y
	elif(b==1):
		z=20
		total = x + y + z
		print ("Entradas", p, ",", s, ",", b)
		print ("Calorias:", total, "cal")
	elif (b==2):
		z=70
		total = x + y + z
		print ("Entradas", p, ",", s, ",", b)
		print ("Calorias:", total, "cal")
	elif (b==3):
		z=100
		total = x + y + z
		print ("Entradas", p, ",", s, ",", b)
		print ("Calorias:", total, "cal")
	elif(b==4):
		z=65
		total = x + y + z
		print ("Entradas", p, ",", s, ",", b)
		print ("Calorias:", total, "cal")
else:
	print ("Entradas", p, ",", s, ",", b)
	print ("Dados invalidos")
