f =input("B ou C:")
qbc = int(input("quantidade de fatias de bolo ou croissant:"))
qc = int(input("quantidade de capuccinos:"))

if(f.upper()=='B'):
	x = qbc*3.0+qc*5.50
	print(round(x, 2))
else:
	x =qbc*6.0+qc*5.50
	print(round(x, 2))

	
	



