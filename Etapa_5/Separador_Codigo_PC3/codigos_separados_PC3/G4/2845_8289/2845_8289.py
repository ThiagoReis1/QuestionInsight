from numpy import * 

sen = array(eval(input(":")))
j = zeros(size(sen), dtype=int)

for i in range(size(sen)):
	if sen[i] != 9:
		j[i] = sen[i] + 1 
	else:
		j[i] = 0

print(j)