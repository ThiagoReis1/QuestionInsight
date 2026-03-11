from numpy import*
nome=array(eval(input("NOMES:")))
quant=array(eval(input("quantidade: ")))
i=0
n=size(nome)
q=size(quant)
A=0
FA=0
B=0
M=0
FE=0
v=""
while(i<n):
	v=nome[i].upper()
	if(v=='ARROZ'):
		A=A+(quant[i]*(1.25))
	if(v=='FEIJAO'):
		FE=FE+(quant[i]*2.60)
	if(v=='BIS'):
		B=B+(quant[i]*1.80)
	if(v=='MIOJO'):
		M=M+(quant[i]*0.85)
	if(v=='FANTA'):
		FA=FA+(quant[i]*3.20)
	i=i+1
print(round(float(A+B+M+FE+FA),2))