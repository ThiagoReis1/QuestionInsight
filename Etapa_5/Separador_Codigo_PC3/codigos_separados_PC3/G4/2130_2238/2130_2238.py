from numpy import*

n = array(eval(input("Notas:")))

mf = ((n[0]*3)+(n[1]*2)+(n[2]*2)+(n[3]*3))/10
print(round(mf,2))
if(mf>=5):
	print("APROVADO")
else:
	print("REPROVADO")