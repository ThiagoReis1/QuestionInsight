altura_joe = 1.77
taxa_joe = 0.02

altura = float(input())
cresc = float(input())
anos = 0
while altura < altura_joe:
	altura += cresc
	anos+=1
	altura_joe+=taxa_joe
	
print(anos)