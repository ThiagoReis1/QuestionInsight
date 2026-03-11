from numpy import*
v = array(eval(input("Vetor de custo dos itens: ")))
desconto=0
i=0
while(i<size(v)):
	if(v[i] > 80):
		desconto=desconto+5
	i = i + 1
	
print(round(sum(v)-desconto,2))

