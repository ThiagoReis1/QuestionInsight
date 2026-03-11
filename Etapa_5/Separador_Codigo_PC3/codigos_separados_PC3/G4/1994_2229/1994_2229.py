#entradas
L=input("Escolha a molecula: ").lower()
#formulas
O=15.9994
C=12.011
N=14.00674
H=1.0079
His=(C*6)+(H*10)+(N*3)+(O*2)
Leu=(C*6)+(H*13)+(N*1)+(O*2)
Lis=(C*6)+(H*15)+(N*2)+(O*2)
#condicao
if(L=="histidina"):
	print(round(His,2))
elif(L=="leucina"):
	print(round(Leu,2))
elif(L=="lisina"):
	print(round(Lis,2))
else:
	print("Entrada:",L)
	print("Dado Invalido")