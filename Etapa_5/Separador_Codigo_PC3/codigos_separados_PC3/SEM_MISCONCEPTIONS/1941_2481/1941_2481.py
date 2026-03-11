nome_do_aminoacido = input("").upper()
O= 15.9994
C = 12.011
N = 14.00674
H = 1.0079
if nome_do_aminoacido == 'GLICINA':
   GLICINA1 = ((C*2) + (H*5) + (N*1) + (O*2))
	print(round(GLICINA1,2))
	
else:
	SERINA1 = (C*3) + (H*7) + (N*1) + (O*3)
	print(round(SERINA1,2))