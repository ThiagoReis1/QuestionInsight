from numpy import*

notas = array(eval(input("Insira as notas: ")))


mfinal = (sum(notas)-max(notas)) /3.0

print(round(mfinal,2))

if(mfinal > 50):
	print("APROVADO")
else:
	print("REPROVADO")