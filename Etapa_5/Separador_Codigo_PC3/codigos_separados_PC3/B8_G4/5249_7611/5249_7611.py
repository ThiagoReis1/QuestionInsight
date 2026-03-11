np = int(input('prato'))
ns = int(input('sobremesa'))
nb = int(input('bebida'))
if (np==1 or np==2 or np==3 or np==4) and (ns==1 or ns==2 or ns==3 or ns==4) and (nb==1 or nb==2 or nb==3 or nb==4):
	if np==1:
		cal = 180
	elif np==2:
		cal = 230
	elif np==3:
		cal=250
	elif np==4:
		cal=350
	if ns==1:
		ca = 75
	elif ns==2:
		ca = 110
	elif ns==3:
		ca = 170
	elif ns==4:
		ca = 200
	if nb==1:
		c=20
	elif nb==2:
		c=70
	elif nb==3:
		c=100
	elif nb==4:
		c=65
		
	print('Calorias:',cal + ca + c,'cal')
else:
	print('Dados invalidos')