from numpy import * 
np = array(eval(input("Notas parciais: ")))

n1 = np[0]
n2 = np[1]
n3 = np[2]

mf = (n1 * 5 + n2 * 2.5 + n3 * 2.5)/10

print(round(mf, 2))

if (mf >= 5):
	print('APROVADO')
elif (mf < 5):
	print('REPROVADO')