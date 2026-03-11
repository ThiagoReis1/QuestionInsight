from numpy import*

a= array(eval(input("notas")))
nf=(a[0]*5+a[1]*3+a[2]*2)/10

print(round(nf,2))

if(nf<=5):
	print("REPROVADO")
else: 
	print("APROVADO")

