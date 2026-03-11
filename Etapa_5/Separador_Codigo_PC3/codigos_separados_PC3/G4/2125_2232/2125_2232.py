from numpy import*
nota=array(eval(input("")))
nf= ((nota[0]*3.0) + (nota[1]*3.0)+ (nota[2]*4.0))/10.0
if(nf > 5.0):
	print(round(nf,2))
	print("APROVADO")
else:
	print(round(nf,2))
	print("REPROVADO")