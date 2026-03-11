from numpy import*
senha = array(eval(input()))
v=zeros(size(senha),dtype=int)
for i in range(size(senha)):
	if senha[i]==0:
		v [i]=9
	else:
		v[i]=senha[i]-1
		
print(v**3)