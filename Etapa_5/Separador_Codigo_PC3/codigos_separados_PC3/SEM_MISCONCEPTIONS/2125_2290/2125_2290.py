from numpy import*

v = array(eval(input("Vetor: ")))

	
nota_final = ((v[0]*3) + (v[1]*3) + (v[2]*4))/10


print(round(nota_final, 2))

if(nota_final >= 5):
	print("APROVADO")
else:
	print("REPROVADO")