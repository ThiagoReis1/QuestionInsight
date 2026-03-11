from numpy import*
v=array(eval(input("Custos: ")))
soma=0
for i in range (size(v)):
	if v[i]>200:
		v[i]=v[i]-v[i]*0.15
	soma=soma+v[i]
print(round(soma,2))