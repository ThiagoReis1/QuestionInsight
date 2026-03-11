from numpy import*
nota = array(eval(input("Digite as notas: ")))
i = 0 
n = nota[0]*1 + nota[1]*2 + nota[2]*3 + nota[3]*4
mfinal = n/10
print(round(mfinal,2))
if (mfinal>5):
	print("APROVADO")
if (mfinal<5):
	print("REPROVADO")