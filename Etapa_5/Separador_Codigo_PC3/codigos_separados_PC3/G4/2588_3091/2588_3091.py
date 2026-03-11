from numpy import*

v=array(eval(input(" ")))

ac=0
#lim = maior que 0.2 do limite e menos que 0.5 do limite
for i in range(size(v)):
	if ((v[i]>(v[0]*0.2 + v[0])) and (v[i]<(v[0]*0.5 +v[0]))):
		ac=ac+1
cop=zeros(ac, dtype=int)	
j=0		
for i in range(size(v)):
	if ((v[i]>(v[0]*0.2 + v[0])) and (v[i]<(v[0]*0.5 +v[0]))):
		cop[j]=i+cop[j]
		j=j+1
print(i)
print(ac)