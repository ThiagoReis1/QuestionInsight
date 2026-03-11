from numpy import*
string = input()
nv = zeros(5,int)
vet = string.split(',')
for x in range(size(vet)):
	if(vet[x]=="CHN"):
		nv[0] = nv[0] + 1
	elif(vet[x]=="JPN"):
		nv[1] = nv[1] + 1
	elif(vet[x]=="KOR"):
		nv[2] = nv[2] + 1
	elif(vet[x]=="MGL"):
		nv[3] = nv[3] + 1
	elif(vet[x]=="THA"):
		nv[4] = nv[4] + 1
print(max(nv))
print(nv)