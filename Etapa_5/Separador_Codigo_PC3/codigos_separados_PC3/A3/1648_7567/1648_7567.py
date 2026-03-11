from numpy import*
freq = array(eval(input("")))
j = 0
k = 0
reprovados = 0
for i in range(size(freq)):
	if(freq[i] < 70):
		reprovados = reprovados + 1

reprovou = zeros(reprovados , dtype = int)
for i in range(size(freq)):
	if(freq[i] < 70):
		reprovou[j] = reprovou[j] + i
		j = j + 1
print(reprovados)
print(reprovou)