altura_joe = 1.77
taxa_joe = 0.07
altura = float(input())
taxa = float(input())
ano = 0
while altura =< altura_joe:
	altura = altura + (altura * taxa)
	altura_joe = altura_joe + (altura_joe * taxa_joe)
	ano +=1
print(ano)
