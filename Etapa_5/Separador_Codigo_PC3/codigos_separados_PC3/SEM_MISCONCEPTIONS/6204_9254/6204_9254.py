altura_macaco = 1.86
taxa_macaco = 0.01
#entrada para a altura do coelho
altura_coelho = float(input("altura coelho: "))
taxa_coelho = float(input("taxa do coelho: "))

i = 0  #variavel contadora para os anos
while altura_coelho <= altura_macaco:
	altura_coelho = altura_coelho +  taxa_coelho
	altura_macaco = altura_macaco +  taxa_macaco
	i = i + 1
print(i)