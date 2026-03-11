from numpy import*
v=array(eval(input("Valores de n: ")))
i=0
r=0
while i<size(v):
	r+=(v[i]**-1)
	i=i+1
m=r/size(v)
print(round(m**-1,2))