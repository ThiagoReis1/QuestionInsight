s=float(input("sitio:"))
d=float(input("deposito:"))
m=float(input("mensal fixo:"))
j=float(input("juros:"))
t=0
k=0
l=0
h=m*(j/100)
if(s>0 and d>0 and m>0 and j>0):
	while(k>0):
		k=s-(d+l)
		t=t+1
		l=l+(m+(m-h))
	print(t)	
else:
	print("Dados incorretos.")
