ami = input("nome do aminoacido: ")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794

if (ami.upper() == "ALANINA"): 
	mensagem = (C * 3)+(H * 7)+(N * 1)+(O * 2)
	print(round(mensagem, 2))
	
else:
	mensagem = (C * 5)+(H * 11)+(N * 1)+(O * 2)
	print(round(mensagem, 2))
	
