from numpy import*
v1=array(eval(input()))
qi=0
j=0

for i in range(size(v1)):
	if v1[i]%2!=0:
		qi+=1
print(qi)
s2=zeros(qi,dtype=int)
for i in range(size(v1)):
	
	if v1[i]%2!=0:
		
		s2[j]=i
		j+=1

print(s2)

		