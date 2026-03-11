x=input("aminoacido: ")
O=15.9994
C=12.011
N=14.00674
H=1.0079
h=((C*6)+(H*10)+(N*3)+(O*2))
l=((C*6)+(H*13)+(N*1)+(O*2))
li=((C*6)+(H*15)+(N*2)+(O*2))
if(x=="histidina"):
	print (round(h, 2))
elif(x=="leucina"):
	print(round(l, 2))
elif(x=="lisina"):
	print(round(li, 2))
else:
	print("Entrada:", x)

	print("Dado Invalido")