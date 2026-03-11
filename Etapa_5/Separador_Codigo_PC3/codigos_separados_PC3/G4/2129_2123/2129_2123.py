me = eval(input("digite o numero: "))
mf = (me[0]*1.0+me[1]*2.0+me[2]*3.0+me[3]*4.0)/10.0
print(round(mf,2))
if(mf>=5):
	print("APROVADO")
else:
	print("REPROVADO")