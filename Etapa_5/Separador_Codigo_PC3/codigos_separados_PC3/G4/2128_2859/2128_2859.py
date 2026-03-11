from numpy import* 

v = array(eval(input("Notas parciais: ")))

m = max(v)
nf = (sum(v) - m)/3
print(round(nf,2))

if(nf >= 50):
	i = "APROVADO"
	
else:
	i = "REPROVADO"
	
print(i)
	

