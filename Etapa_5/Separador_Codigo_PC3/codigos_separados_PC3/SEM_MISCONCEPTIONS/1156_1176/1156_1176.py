numcel= float(input("Digite a quantidade de células cancerosas:"))
taxa= float(input("Digite a taxa percentual de reudacao:"))
numnovo= int(input("Digite o numero de novas celulas cancerosas:"))
soma= ((numcel*taxa)-numcel)+ numnovo
conte=0
while (soma >= 500000):
		conte= conte+1
		numnovo= print("Digite o numero de novas celulas cancerosas:")
		numcel= soma
		soma= ((numcel*taxa)-numcel)+ numnovo
		print(conte)		