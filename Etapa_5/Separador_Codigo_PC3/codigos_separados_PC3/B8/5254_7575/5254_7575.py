p=float(input("preco do produto: "))
c=int(input("codigo da regiao: "))

if(c==1):
	print(p-(p*0.4)+p*(10/100))
elif(c==2):
	venda=p-(p*0.4)+(p*(8/100))
	print(round(venda,2))
elif(c==3):
	venda=p-(p*0.4)+(p*(0/100))
	print(round(venda,2))
elif(c==4):
	venda=p-(p*0.4)+(p*(2/100))
	print(round(venda,2))