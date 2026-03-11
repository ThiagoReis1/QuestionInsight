from numpy import*
x=array(eval(input("numeros.")))
p=0 #acumuladora de impares
n=0#para o tamanho do vetor zero
s=-1
for i in range(size(x)):
	if(x[i]%2!=0):
		p=p+1
for l in range(size(x)):
	if(x[l]%2!=0):
		n=n+1
w=zeros(n,dtype=int)
for y in range(size(x)):
	if(x[y]%2!=0):
		s=s+1
		w[s]=y
print(p)
print(w)