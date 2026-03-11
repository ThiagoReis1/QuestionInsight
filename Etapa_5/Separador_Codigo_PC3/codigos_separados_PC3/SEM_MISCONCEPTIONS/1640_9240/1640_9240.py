from numpy import*

vetor = array(eval(input("Primeiro vetor: ")))

par = 0
impar = 0

while (size(vetor) > 1):
	for elementos in vetor:
		if(elemento % 2 == 0):
			impar = impar + 1
		else:
			impar += 1
			
print(impar)
print(par)
print(len(vetor))

vetor = array (eval(input("Proximo vetor: ")))

par = 0
impar = 0