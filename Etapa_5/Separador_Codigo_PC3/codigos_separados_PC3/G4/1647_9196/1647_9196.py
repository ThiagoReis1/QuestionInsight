from numpy import*

f= array(eval(input("frequencias:")))
k=0

for i in range(size(f)):
	if f[i] >= 70:
		k+=1
		
f1= zeros(k,dtype=int)
j= 0 
for i in range(size(f)):
	if f[i] >= 70:
		f1[j] = i
		j+=1
print(k)

print(f1)