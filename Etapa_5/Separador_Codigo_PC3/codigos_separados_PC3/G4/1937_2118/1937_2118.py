nome = input("nome: ")

o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794

conta1 = (3 * c) + (7 * h) + n + (2 * o)
conta2 = (5 * c) + (11 * h) + n + (2 * o)
 
if (nome == "Alanina".upper()):
	print(round(conta1, 2))
	
else:
	print(round(conta2, 2))