from numpy import *

nta=array(eval(input()))
vps=array([1,3,2,5])

nm=nta*vps
md=sum(nm)/sum(vps)
print(round(md,2))