altura_macaco = 1.86
taxa_macaco = 0.01

total = 0

altura= float(input())
taxa = float(input())

while (altura < altura_macaco):
	altura = altura + taxa 
	altura_macaco = altura_macaco + taxa_macaco
	total = total + 1
print(total)