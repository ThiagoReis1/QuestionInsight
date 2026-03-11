from numpy import*

notas= array(eval(input("")))
i= 0
j= 0
imp= 0

for i in range(size(notas)):
	if (notas[i] % 2) != 0 :
		imp+=1
nov= zeros(imp, dtype=int)
for i in range(size(notas)):
	if (notas[i] %2 ) != 0:
		nov[j]= i 
		j +=1
print(imp)
print(nov)