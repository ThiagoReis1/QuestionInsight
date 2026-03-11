bola=input("cor da bola")
bola=bola.upper()
contagem=0
while bola!="S":
	if bola=="PRETA":
		contagem = contagem+1
	bola=input("cor da bola")
print(contagem)