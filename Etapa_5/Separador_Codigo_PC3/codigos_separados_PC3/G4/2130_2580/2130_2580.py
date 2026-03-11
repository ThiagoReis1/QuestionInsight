from numpy import*
x=array(eval(input("notas: ")))
m=((x[0]*3.0+x[1]*2.0+x[2]*2.0+x[3]*3.0)/10)
if(m>=5.0):
	msg="APROVADO"
else:
	msg="REPROVADO"
print(round(m,2))
print(msg)