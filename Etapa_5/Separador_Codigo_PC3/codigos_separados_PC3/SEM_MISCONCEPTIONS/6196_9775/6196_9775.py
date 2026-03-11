altura_chico = 1.5
taxa_chico = 0.02

altura_pedro = float(input())
taxa_pedro = float(input())

years = 0

while altura_chico > altura_pedro:
	altura_chico += taxa_chico
	altura_pedro += taxa_pedro
	
	years += 1
print(years)