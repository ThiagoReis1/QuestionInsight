L = input("Insira o nome da molecula: ") .lower()
#Entradas
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

his = (C*6) + (H*10) + (N*3) + (O*2)
leu = (C*6) + (H*13) + (N*1) + (O*2)
lis = (C*6) + (H*15) + (N*2) + (O*2)

#Condicao
if(L == "histidina"):
	print(round(his, 2))
elif(L == "leucina"):
	print(round(leu, 2))
elif(L == "lisina"):
	print(round(lis, 2)) 
else:
	print("Entrada: ",L)
	print("Dado Invalido")