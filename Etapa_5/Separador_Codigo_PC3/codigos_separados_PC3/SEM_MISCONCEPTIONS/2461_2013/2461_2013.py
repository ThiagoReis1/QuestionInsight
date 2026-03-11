v=float(input("valor da mercadoria:"))

#1
if (v<=50):
	lucro=v+((v*100)/100)
	print(round(lucro,2))
elif (v>=50.01)and(v<=100) :
	lucro=v+((v*50)/100)
	print(round(lucro,2))
elif (v>=100.01) and (v<=500):
	lucro=v+((v*40)/100)
	print(lucro)
else:
	lucro=v+((v*30)/100)
	print(round(lucro,2))