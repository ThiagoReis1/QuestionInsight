from numpy import*
n = array(eval(input("")))

nf = (n[0]*3 + n[1]*3 + n[2]*4)/10

print(round(nf,2))
if(nf >= 5):
	print("APROVADO")
else:
	print("REPROVADO")