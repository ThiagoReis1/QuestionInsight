from numpy import*
ch = array(eval(input("carga horaria")))

s=0
for i in range(size(ch)):
	if(ch[i]>=70):
		s+=1

print(s)
j =0
k = zeros(s,dtype=int)
for i in range(size(ch)):
	if(ch[i]>=70):
		k[j]=i
		j+=1
print(k)

		 