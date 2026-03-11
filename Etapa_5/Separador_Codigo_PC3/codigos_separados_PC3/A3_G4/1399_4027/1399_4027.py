qAR=int(input("Quantidade de votos para o candidato Ambrosio Rutra: "))
qDO=int(input("Quantidade de votos para o candidato Demelza Olecram: "))
T= qAR +qDO
if(qAR > qDO):
	print("Ambrosio Rutra")
	p=(qAR/T)*100
if(qDO > qAR):
	print("Demelza Olecram")
	p=(qDO/T)*100
print(round(p, 2))