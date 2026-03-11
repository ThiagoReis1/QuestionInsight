from numpy import*
vetor = array(eval(input("alo: ")))
pesos = [5,4,3,2]
new = zeros(size(vetor),dtype=int)
i=0

while i<size(vetor):
	new[i] = vetor[i]*pesos[i]
	i=i+1
	
media = sum(new)/sum(pesos)
print(round(media,2))