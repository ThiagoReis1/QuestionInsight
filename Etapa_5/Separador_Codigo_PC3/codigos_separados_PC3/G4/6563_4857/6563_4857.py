# faça seu código aqui!
d= float(input("Quantidade de dias: "))

if(d <15):
	v = (175*d)+20
	print("total=",round(v,2))
elif(d == 15):
	v=(175*d)+16
	print("total=",round(v,2))
else:
	v=(175*d)+10
	print("total=",round(v,2))
	