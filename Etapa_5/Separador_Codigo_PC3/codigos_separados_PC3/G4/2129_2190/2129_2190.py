from numpy import*

n = array(eval(input()))

mf = (n[0*1] + n[1]*2 + n[2]*3 + n[3]*4)/10
print(round(mf,2))
if(mf >= 5):
	print("APROVADO")
else:
	print("REPROVADO")