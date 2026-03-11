from numpy import*

notas = array(eval(input("Digite o vetor nota: ")))
i=0
soma=0
menor = min(notas)
while(i<size(notas)):
	soma = soma + notas[i]
	i = i +1
media = (soma-menor)/(size(notas)-1)
print(round(media,2))
	

	

