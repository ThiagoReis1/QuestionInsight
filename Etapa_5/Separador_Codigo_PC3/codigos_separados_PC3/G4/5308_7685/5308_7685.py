x= float(input("x: "))
k= int(input("k: "))
soma=0
i=1
f=(i*1)/(2*i*x)

while(k>=i and x!=0 and k>0):
	soma=soma+f
	i=i+1
	
print(round(soma,10))