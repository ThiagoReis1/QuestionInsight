from numpy import*

nt = array(eval(input("Notas parciais: ")))

Nota0 = nt[0]
Nota1 = nt[1]
Nota2 = nt[2]

NF = (Nota0 * 2.0 + Nota1 * 3.0 + Nota2 * 5.0) / 10.0
print(round(NF,2))

if NF > 5:
	print("APROVADO")
else:
	print("REPROVADO")