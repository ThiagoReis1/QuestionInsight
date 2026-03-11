from numpy import*
v=array(eval(input()))
p=[5,1]
m=((v[0]*p[0])+(v[1]*p[1]))/sum(p)
print(round(m,2))
