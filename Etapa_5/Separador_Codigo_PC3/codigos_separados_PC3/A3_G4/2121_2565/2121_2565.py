from numpy import*
n = array(eval(input("")))

m = (sum(n) - max(n))
#calculo da nota final
nf = ((n[0]*5.0) + (n[1]*3.0) + n[2]*2.0)/10.0

print(round(nf, 2))

if(nf >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")
		
