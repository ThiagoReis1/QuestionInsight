altura_macaco = 1.86
taxa_macaco = 0.01

altura_cueio = float(input())
taxa_cueio = float(input())

year = 0

while(altura_macaco > altura_cueio):
	altura_macaco = altura_macaco + taxa_macaco
	altura_cueio = altura_cueio + taxa_cueio
	year += 1
print(year)