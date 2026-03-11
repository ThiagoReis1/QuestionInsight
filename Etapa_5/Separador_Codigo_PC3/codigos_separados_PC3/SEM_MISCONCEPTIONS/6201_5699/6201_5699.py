altura_joe = 1.77
taxa_joe = 0.02

altura_outro = float(input())
taxa_outro = float(input())
anos = 0

while altura_joe > altura_outro:
	altura_joe += taxa_joe
	altura_outro += taxa_outro
	anos += 1

print(anos)