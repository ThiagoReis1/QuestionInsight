nome = input("nome: ")

O= 15.9994
C= 12.011
N= 14.00674
H= 1.00794

conta1= (3 * C) + (7 * H) + N + (2 * O) 

conta2= (5 * C) + (11 * H) + N + (2 * O)

if nome== ("alanina".upper()):
	print(round(conta1,2))
else:
	print(round(conta2,2))