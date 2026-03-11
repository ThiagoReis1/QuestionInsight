from numpy import*

t = input("cor dos olhos: ")
vet = t.split(',')
p = 0
c = 0
m = 0
v = 0
a = 0
for i in range(size(vet)):
	if(vet[i]=="P"):
		p = p + 1
	elif(vet[i]=="C"):
		c = c + 1
	elif(vet[i]=="M"):
		m = m + 1
	elif(vet[i]=="V"):
		v = v + 1
	else:
		a = a + 1
print(max(p,c,m,v,a))

vcont = zeros(5, dtype=int)
for i in range(size(vet)):
	if(vet[i] == "P"):
		vcont[0] = vcont[0] + 1
	elif(vet[i]=="C"):
		vcont[1] = vcont[1] + 1
	elif(vet[i]=="M"):
		vcont[2] = vcont[2] + 1
	elif(vet[i]=="V"):
		vcont[3] = vcont[3] + 1
	else:
		vcont[4] = vcont[4] + 1
print(vcont)
	
	

	
	



