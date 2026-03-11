from numpy import*

notas= array(eval(input("Insira as notas dos alunos: ")))


j= 0 
c= 0 

for i in range(size(notas)):
	if notas[i] < 5:
		c= c + 1
print(c)

zeros= zeros(c, dtype=int)

for i in range(size(notas)):
	if notas[i] < 5:
		zeros[j]= i 
		j= j + 1 
print(zeros)
		

	
