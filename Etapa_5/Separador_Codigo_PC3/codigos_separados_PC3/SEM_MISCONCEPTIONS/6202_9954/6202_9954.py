altura_bia = 1.69
taxa_bia = 0.01

altura = float(input())
taxa = float(input())

i = 0

while altura <= altura_bia:
	altura_bia += taxa_bia
	altura += taxa
	i+=1
print(i)