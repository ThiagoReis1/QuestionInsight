from numpy import*
gostastes = array(eval(input("Digite agora: ")))
pesos = [5,4,3,2]
new = zeros(size(gostastes),dtype=int)
i = 0

while i < size(gostastes):
	new[i] = gostastes[i]*pesos[i]
	i += 1
media = sum(new)/sum(pesos)
print(round(media,2))

