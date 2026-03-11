qntvot1=int(input("Digite a quantidade de votos para Ambrosio Rutra: "))
qntvot2= int(input("DIgite a quantidade de votos para Demelza Olecram: "))

total= (qntvot1 + qntvot2)
totalam= (total-qntvot2)*0.1
totalde= (total-qntvot1)*0.1


if(qntvot1>qntvot2):
	print("Ambrosio Rutra")
	mensa= totalam
else: 
	print("Demelza Olecram")
	mensa= totalde
	
print(round(mensa, 2))
