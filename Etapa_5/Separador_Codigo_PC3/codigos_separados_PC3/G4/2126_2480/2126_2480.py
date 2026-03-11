from numpy import*
v = array(eval(input("Notas: ")))
m = (v[0]  *5 + v[1]  *2.5 + v[2]* 2.5) /10
print(round(m,2))
if (m > 5):
	print("APROVADO")
else:
	print("REPROVADO")