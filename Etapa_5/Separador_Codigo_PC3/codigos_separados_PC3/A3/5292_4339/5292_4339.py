jogadas= input("cor da cas").upper()
contp=0
contv=0
contf=0
porc=0.0
while (jogadas != "S") :
	if(jogadas == "PRETA"):
		contp= contp + 1
	if(jogadas == "VERMELHA"):
		contv= contv + 1
	jogadas= input("cor da casa:").upper()
	contf= contp + contv
if (contp > 0):
	porc= 100 * contp/contf
	
print(contf)
print(round(porc,2))
