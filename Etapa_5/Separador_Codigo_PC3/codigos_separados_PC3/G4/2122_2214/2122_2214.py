from numpy import*

a = array(eval(input("Notas: ")))

nf = (a[0]*2+a[1]*3+a[2]*5)/10

print(round(nf,2))
if(nf<=5):
	print("REPROVADO")
else:
	print("APROVADO")

