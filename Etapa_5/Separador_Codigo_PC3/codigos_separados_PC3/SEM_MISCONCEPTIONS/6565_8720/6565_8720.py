# faça seu código aqui!
dist=int(input())
if(dist<10):
	tx=5.50
elif(dist==10):
	tx=7.75
else:
	tx=10.00
valor=50+tx
print("total=",round(valor, 2))