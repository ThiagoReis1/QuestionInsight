from numpy import*
vet = input("").split(',')
t = zeros(5,dtype=int)
for i in vet :
	if(i == "CHN"):
		t[0] = t[0] + 1
	if(i == "JPN"):
		t[1] = t [1] + 1
	if(i == "KOR"):
		t[2] = t[2] + 1
	if(i == "MGL"):
		t[3] = t[3] + 1
	if(i == "THA"):
		t[4] = t[4] + 1
print(max(t))
print(t)
