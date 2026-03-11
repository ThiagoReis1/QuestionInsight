from numpy import*
vetorpeso = array(eval(input("Digite vetor peso: ")))
vetoraltura = array(eval(input("Digite o vetor altura: ")))
l=[]
vetorImc=array(range(len(vetorpeso)))
for i in range(len(vetorpeso)):
	l.append(round(vetorpeso[i]/(vetoraltura[i]*vetoraltura[i]),2))
l=array(l)
print(l)

print("")