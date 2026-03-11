from numpy import*
v=array(eval(input()))
n=array([3,4,2,1,4,5])

v0= v*n
print(round(sum(v0)/sum(n), 2))
