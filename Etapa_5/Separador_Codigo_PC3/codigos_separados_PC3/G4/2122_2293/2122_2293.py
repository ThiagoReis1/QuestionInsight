from numpy import*
n = array(eval(input("Vetor nota: ")))
n0 = n[0]
n1 = n[1]
n2 = n[2]
med = (n0*2 + n1*3 + n2 * 5)/10
print(med)
if(med>=5):
	print("APROVADO")
else:
	print("REPROVADO")
	
