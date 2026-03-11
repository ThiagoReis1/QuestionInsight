from numpy import*
v=array(eval(input("Digite as notas")))
no=float(v[0])
n1=float(v[1])
n2=float(v[2])
mf=(no*5.0+n1*2.5+n2*2.5)/10
print(round(mf,2))
if(mf>=5):
	print("APROVADO")
else:
	print("REPROVADO")
	
	