from numpy import*
vetor = array(eval(input("Digite um vetor:")))
resultado = []
c = 0
for i in range(size(vetor)):
	if vetor[i] >= 2000:
		c = c+1
		resultado = resultado +[i]
	
print(c)
print(array(resultado))