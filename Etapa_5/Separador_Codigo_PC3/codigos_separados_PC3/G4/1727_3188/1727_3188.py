from numpy import*
from numpy.linalg import*

mat=array(eval(input()))

vz=zeros(mat.shape[1])


for i in range(mat.shape[1]):
	vz[i]=max(mat[:,i])		
	
print(max(vz))	