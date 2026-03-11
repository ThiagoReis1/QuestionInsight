from numpy import*

ap=array(eval(input()))
qt=0

for i in range(size(ap)):
	if ap[i]>=70:
		qt+=1
ip=[0]*qt
j=0
for i in range(len(ap)):
	if ap[i]>=70:
		ip[j]=i
		j+=1
print(qt)
print(array(ip))