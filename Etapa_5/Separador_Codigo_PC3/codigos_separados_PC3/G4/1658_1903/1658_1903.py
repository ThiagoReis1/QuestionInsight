from numpy import*

vet = input("vet: ")

nv = vet.split(',')

p = zeros(5, dtype = int)

for i in range(size(nv)):
	if(nv[i] == "CHN"):
		p[0] += 1
	if(nv[i] == "JPN"):
		p[1] += 1
	if(nv[i] == "KOR"):
		p[2] += 1
	if(nv[i] == "MGL"):
		p[3] += 1
	if(nv[i] == "THA"):
		p[4] += 1
		
print(max(p))
print(p)