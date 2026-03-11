from numpy import*
v= array(eval(input("vetor")))
a=0
for x in v:
	if(x>=70):
		a=a+1
print(a)	
copia= zeros(a, dtype=int)
i=0
for x in range(size(v)):
	if v[x]>=70:
		copia[i]=x
		i=i+1
print(copia)
		