#nota final são 3 notas: provas, trabalhos e seminarios
#notas variam de 0 a 10
#formula : NF = (s[0] *3.0 + s[1]*3.0 + s[2]*4.0)/10.0
from numpy import *
s = array(eval(input("Quais são as notas? ")))
nf = (s[0] *3.0 + s[1]*3.0 + s[2]*4.0)/10.0
if (nf>=5.0):
	print(round(nf,2))
	print("APROVADO")
else:
	print(round(nf,2))
	print("REPROVADO")