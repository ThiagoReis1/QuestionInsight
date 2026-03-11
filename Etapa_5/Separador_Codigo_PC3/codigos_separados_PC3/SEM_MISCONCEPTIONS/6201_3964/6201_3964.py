altura_joe = 1.77
taxa_joe = 0.02

altura = float(input())
taxa = float(input())

anos = 0

while altura < altura_joe:
	altura = altura+taxa
	altura_joe = altura_joe+taxa_joe
	anos+=1
	
print(anos)