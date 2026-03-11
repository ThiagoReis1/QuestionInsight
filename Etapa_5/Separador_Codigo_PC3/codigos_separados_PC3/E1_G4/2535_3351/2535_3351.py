da = float(input("Insira o investimento A: "))
db = float(input("Insira o investimento B: "))
ta = float(input("Insira a taxa de juros do Banco A: "))/100
tb = float(input("Insira a taxa de juros do Banco B: "))/100
#Acumulando Grana
ma = da 
mb = db
#Acumulando tempo
mes = 0
if(da >0 and db>0 and ta>0 and tb>0 and da>db and ta<tb):
	while(ma > mb):
		ma = round(ma + ma*ta,2)
		mb = round(mb + mb*tb,2)
		mes = mes + 1
	print(mes)
else:
	print("Dados incorretos")