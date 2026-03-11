from numpy import* 
gos = array(eval(input("digite")))
pesos = (5,4,3,2)
b = zeros(size(gos), dtype = float)

i = 0

while i < size(gos):
	b[i] = gos[i] * pesos[i]
	i += 1 
media = sum(b)/sum(pesos)
print(round(media,2))	



