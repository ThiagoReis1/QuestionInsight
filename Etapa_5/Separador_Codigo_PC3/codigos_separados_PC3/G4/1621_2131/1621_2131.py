from numpy import*

a=array(eval(input("nome dos produtos: ")))
b=array(eval(input("quantidades: ")))
i = 0
v1 = 0
while(i<size(a)):
	if(a[i]=="ARROZ"):
		v1 = v1 + b[i] * 1.25
	if(a[i]=="FEIJAO"):
		v1 = v1 + b[i] * 2.60
	if(a[i]=="BIS"):
		v1 = v1 + b[i] * 1.80
	if(a[i]=="MIOJO"):
		v1 = v1 + b[i] * 0.85
	if(a[i]=="FANTA"):
		v1 = v1 + b[i] * 3.20
	i=i+1
print(round(v1,2))

