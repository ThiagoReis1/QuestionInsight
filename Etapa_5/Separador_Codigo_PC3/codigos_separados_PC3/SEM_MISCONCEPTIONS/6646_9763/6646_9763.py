from numpy import*
m = array(eval(input("informe as medias: ")))
vetor = array ([1,2,3])
f = size(m)
i = 0
s = 0

while i < f:
	media = m[i] * vetor[i]
	s = s + media
	i = i + 1
print(round(s/sum(vetor), 2))
