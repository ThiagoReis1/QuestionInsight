from numpy import*

n = array(eval(input("notas: ")))

nf = ((n[0]*2) + (n[1]*3) + (n[2]*5))/10

if(nf<5):
	s = "REPROVADO"
else:
	s = "APROVADO"

print(round(nf,2))
print(s)