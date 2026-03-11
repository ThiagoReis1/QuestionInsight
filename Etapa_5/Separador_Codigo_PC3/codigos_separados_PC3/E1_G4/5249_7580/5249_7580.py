p1 = int(input(': '))
p2 = int(input(': '))
p3 = int(input(': '))
w = 0
if p1<1 or p1>4 or p2>4 or p2<1 or p3<1 or p3>4:
	print('Dados invalidos')
else:
	if p1 == 1:
		w += 180
	elif p1 ==2:
		w += 230
	elif p1 ==3:
		w += 250
	else:
		w += 350
	if p2 ==1:
		w += 75
	elif p2 ==2:
		w += 110 
	elif p2 ==3:
		w += 170
	else:
		w += 200
	if p3 == 1:
		w += 20
	elif p3 == 2:
		w += 70
	elif p3 == 3:
		w += 100
	else:
		w += 65
	print('Calorias: {} cal'.format(w))