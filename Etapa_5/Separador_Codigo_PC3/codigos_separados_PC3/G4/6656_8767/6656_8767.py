from numpy import*

vet = array(eval(input("")))
i = 0
p = array([3,4,2,1,4,5])
u = vet[0] * p[0] + vet[1] * p[1] + vet[2] * p[2] + vet[3] * p[3] + vet[4] * p[4] + vet[5] * p[5]
media = u / sum(p)
i = i + 1		
			 			 
print(round(media,2))