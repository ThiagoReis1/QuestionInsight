from numpy import*
x = array(eval(input("")))
mf = (x[0]*3.0 + x[1]*2.0 + x[2]*2.0 + x[3]*3.0)/10.0 
print(round(mf,2))
if mf >= 5:
	print("APROVADO")
else:
	print("REPROVADO")

