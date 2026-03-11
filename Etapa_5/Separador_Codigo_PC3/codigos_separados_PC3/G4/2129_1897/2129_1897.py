from numpy import*

x=array(eval(input("Notas: ")))

nota = (x[0]+(2*x[1])+(3*x[2])+(4*x[3]))/10.0
print(round(nota,2))
if(nota>=5):
	print("APROVADO")
else:
	print("REPROVADO")