aminoacido = input("qual o nome do aminoacido: ")
O = 15.999
C = 12.011
N = 1.00794
H = 1.00794
if (aminoacido.upper() == "ASPARAGINA"):
   mensagem = (C * 4)+(H * 8)+(N * 2)+(O * 3)
	print(round(mensagem, 2))
else: 
	mensagem = (C * 11)+(H * 11)+(N * 2)+(O * 2)	
	print(round(mensagem, 2))				 