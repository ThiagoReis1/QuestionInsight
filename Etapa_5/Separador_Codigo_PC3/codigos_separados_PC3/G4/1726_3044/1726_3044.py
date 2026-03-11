from numpy import*
mat=array(eval(input("matriz: ")))
z=zeros(mat.shape[0])
for i in range(0,mat.shape[0]):
	z[i]=min(mat[i,:])
	
print(min(z))
