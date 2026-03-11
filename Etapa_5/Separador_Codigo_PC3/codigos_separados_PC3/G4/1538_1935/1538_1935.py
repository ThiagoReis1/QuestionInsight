x= float(input(":"))
k=   int(input(":"))
soma=0
cont=0
while(k>cont):
	soma=soma+((-1)**cont)*(x**(cont*2))
	cont=cont+1
	
print(round(soma,8))