#leia: 
#quantidade de votos Ambrosio = qva
#quantidade de votos Demelza = qvd

qva = int(input("Digite a quantidade de votos para Ambrosio: "))
qvd = int(input("Digite a quantidade de votos para Demelza: "))

total = qva + qvd

#saida: prin(nome do vencedor)
if((qva/total) > 0.5):
	m = "Ambrosio Rutra"
	pv = (qva / total)*100
else:
	m = "Demelza Olecram"
	pv = (qvd / total)*100
print(m)
print(round(pv,2))