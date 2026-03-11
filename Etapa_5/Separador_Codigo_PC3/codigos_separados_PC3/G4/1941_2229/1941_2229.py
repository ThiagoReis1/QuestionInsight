#entrada
M=input("escolha: ")

#formula
O=15.9994
C=12.011
N= 14.00674
H= 1.0079

G=(C*2)+(H*5)+N+(O*2)
S=(C*3)+(H*7)+N+(O*3)

#condicao
if(M.upper()=="GLICINA"):
	print(round(G,2))
	
else:
	print(round(S,2))