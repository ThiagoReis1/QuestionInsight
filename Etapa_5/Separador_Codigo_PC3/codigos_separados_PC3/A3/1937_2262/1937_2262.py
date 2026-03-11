ALANINA = input("aminoacido: ")
O = 15.994
C = 12.011
N = 14.00674
H = 1.00794
if(aminoacido == "ALANINA"):
   mensagem = 5*C + 11*H + N + 2*O
else:
	mensagem = 3*C + 7*H + N + 2*O
print(round(mensagem, 2))



