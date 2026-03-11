from numpy import*
v=array(eval(input("vetor")))
s=0
for i in range(size(v)):  
	s=s+v[i]
s=(s-min(v))/(size(v)-1)
print(round(s,2))
