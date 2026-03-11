from numpy import*
vn=array(eval(input()))
s=size(vn)
u=s-1
x=sum(vn)
y=min(vn)
z=x-y
m=z/u
print(round(m, 2))
