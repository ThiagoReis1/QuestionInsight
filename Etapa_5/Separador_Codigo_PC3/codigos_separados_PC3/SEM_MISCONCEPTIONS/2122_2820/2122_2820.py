from numpy import*
a=array(eval(input(" ")))
Nota0=a[0]
Nota1=a[1]
Nota2=a[2]
NF = (Nota0 * 2.0 + Nota1 * 3.0 + Nota2 * 5.0) / 10.0
if(NF>=5):
	print(NF)
	print("APROVADO")
else:
	print(NF)
	print("REPROVADO")