from numpy import * 

notas = array(eval(input("notas: ")))
i = 0

for x in range(size(notas)):
	if(notas[x] < 5):
		i = i + 1
print(i)	
j = 0
for x in range(size(notas)):
	if(notas[x] < 5):
		j = j + x
		print(j)
		


		