v= int(input())
c= int(input())
j= float(input())

tempo=0
if(v>0 and c>0 and j>0):
	while(saldo<=(v*1/2)):
		saldo= v - c 
		saldo= saldo*j
		tempo= tempo+1
	print(round(tempo,2))
else:
	"Dados incorretos"