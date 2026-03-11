p=float(input("preco: "))
c=int(input("codigo: "))
if(c==1):
	f=0.1
	venda=(p-p*0.1)+p*(f/100)
	print(round(venda,2))
if(c==2):
	f=0.08
	venda=(p-p*0.)+p*(f/100)
	print(round(venda,2))
if(c==3):
	f=gratis
	venda=(p-p*0.4)+p*(f/100)
	print(round(venda,2))
if(c ==4):
	f=0.02
	venda=(p-p*0.4)+p*(f/100)
	print(round(venda,2))

