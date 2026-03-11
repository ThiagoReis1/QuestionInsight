n=int(input('numero: '))
i=0
m=''
while(n!=0):
	if(n>0):
		m=m+' POSITIVO'
	elif(n<0):
		m=m+' NEGATIVO'
	i=i+1
	n=int(input('numero: '))
print(m)