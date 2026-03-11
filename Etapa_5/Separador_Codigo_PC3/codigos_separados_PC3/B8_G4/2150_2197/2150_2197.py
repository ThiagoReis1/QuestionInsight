from numpy import*
time = array(eval(input("Digite times de futebol cariocas: ")))
cont = zeros(4,dtype=int)

for i in range(size(time)):
	if time[i] == 'BOTAFOGO':
		cont[0] = cont[0] + 1
	elif time[i] == 'FLAMENGO':
		cont[1] = cont[1] + 1
	elif time[i] == 'FLUMINENSE':
		cont[2] = cont[2] + 1
	elif time[i] == 'VASCO':
		cont[3] = cont[3] + 1
print(cont)