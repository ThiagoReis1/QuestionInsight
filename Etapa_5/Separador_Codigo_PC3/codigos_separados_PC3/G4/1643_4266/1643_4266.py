from numpy import*

n = array(eval(input("Digite o vetor nota: ")))
c=0
j=0
p=0
for i in n:
	if (i>=5):
		c=c+1
v=zeros(c,dtype=int)
for i in n:
	if (i>=5):
		v[j]=p
		j=j+1
	p=p+1
print(c)
print(v)