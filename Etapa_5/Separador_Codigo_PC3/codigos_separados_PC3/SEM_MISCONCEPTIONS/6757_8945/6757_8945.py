num = int(input("Digite"))
taxa_fixa = 5

if num < 3:
	tad = 3.00
	
elif num == 3:
	tad = 3.25
	
else:
	tad = 4.50
	
custo_total = num * taxa_fixa + tad

custo_total = round(custo_total, 2)

print(custo_total)