di=float(input())
m=int(input())

cont=0

while(cont<m):
	di=di+(di*1.2/100)
	print(round(di,2))
	cont=cont+1
