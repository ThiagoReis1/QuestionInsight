from numpy import *
nota = array(eval(input("Digite a nota: ")))
x = nota [0]
y = nota [1]
z = nota [2]
nota_final = (x * 5.0 + y * 3.0 + z * 2.0)/10.0  
print(nota_final)
if(nota_final >= 5.0):
	ap = "APROVADO"
	print("APROVADO")
else:
	print("REPROVADO")