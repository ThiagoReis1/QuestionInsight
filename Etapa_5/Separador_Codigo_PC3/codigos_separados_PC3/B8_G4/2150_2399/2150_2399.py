from numpy import*

nome = array(eval(input()))
v= zeros(4, dtype=int)

b=0
fla=0
flu=0
va=0

for i in range(size(nome)):
	if(nome[i] == "BOTAFOGO"):
		b=b+1
	elif(nome[i] == "FLAMENGO"):
		fla=fla+1
	elif(nome[i] == "FLUMINENSE"):
		flu=flu+1
	elif(nome[i] == "VASCO"):
		va=va+1

		
v[0] = b
v[1] = fla
v[2] = flu
v[3] = va
print(v)