from numpy import*
s = array(eval(input(": ")))
cont = zeros(4,dtype=int)

for i in range(size(s)):
	if(s[i] == "BOTAFOGO"):
		cont[0] = cont[0] + 1
	elif(s[i] == "FLAMENGO"):
		cont[1] = cont[1] + 1
	elif(s[i] == "FLUMINENSE"):
		cont[2] = cont[2] + 1
	elif(s[i] == "VASCO"):
		cont[3] = cont[3] + 1
print(cont)