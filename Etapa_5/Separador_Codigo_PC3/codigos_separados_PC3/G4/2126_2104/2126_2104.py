from numpy import*
me = eval(input("nova cumpati:"))
mf = (me[0]*5.0+me[1]*2.5+me[2]*2.5)/10
print(round(mf,2))
if(mf>5):
	print("APROVADO")
else:
	print("REPROVADO")