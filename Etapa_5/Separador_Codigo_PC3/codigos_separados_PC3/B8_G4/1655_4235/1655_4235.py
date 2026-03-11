from numpy import*
s = input()
vet = s.split(',')
pp = zeros(5, dtype=int)
for i in range(size(vet)):
	if(vet[i]=='AC'):
		pp[0]= pp[0]+1
	elif(vet[i]=='AM'):
		pp[1]=pp[1]+1
	elif(vet[i]=='PA'):
		pp[2]= pp[2]+1
	elif(vet[i]=='RO'):
		pp[3]= pp[3]+1
	elif(vet[i]=='RR'):
		pp[4]= pp[4]+1
print(max(pp))
		
p = zeros(5,dtype=int)
for i in range(size(vet)):
	if(vet[i]=='AC'):
		p[0]= p[0]+1
	elif(vet[i]=='AM'):
		p[1]=p[1]+1
	elif(vet[i]=='PA'):
		p[2] = p[2]+1
	elif(vet[i]=='RO'):
		p[3]= p[3]+1
	elif(vet[i]=='RR'):
		p[4]= p[4]+1
print(p)
