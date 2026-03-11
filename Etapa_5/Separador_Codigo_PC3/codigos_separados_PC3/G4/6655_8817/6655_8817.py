from numpy import*

a = array(eval(input()))
v = [5,1] 

t = ((a[0] * v[0]) + (a[1]*1))/sum(v)
print(round(t,2))