from numpy import*
vetor=array(eval(input(">>>>> ")))
a=0
for i in range(size(vetor)):
	if vetor[i]>=2000:
		a=a+1
b=0
vv=zeros(size(vetor),dtype=int)
for i in range(size(vetor)):
	if vetor[i]>=2000:
		vv[i]=i
		b=vv
print(a)
print(b)