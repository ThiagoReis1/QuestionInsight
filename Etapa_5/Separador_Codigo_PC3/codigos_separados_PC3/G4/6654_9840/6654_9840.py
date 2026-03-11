from numpy import*
v= eval(input("manda:"))
r=[1,3,2,5]
tamy=size(r)
i=0
c=0
while i<tamy:
	m=v[i]*r[i]
	c=c+m
	i+=1
print(round(c/sum(r),2))