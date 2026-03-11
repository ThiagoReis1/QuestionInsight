from numpy import*
v = array(eval(input("")))
me = sum(v) - min(v)
mf = me/3
if (mf>=50.0):
	print(round(mf,2))
	print("APROVADO")
else:
	print(round(mf,2))
	print("REPROVADO")
