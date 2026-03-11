altura_macaco = 1.4
taxa_macaco = 0.06
count = 0
alt_leao = float(input())
taxa_leao = float(input())

while altura_macaco < alt_leao:
	altura_macaco = altura_macaco + taxa_macaco
	alt_leao = alt_leao + taxa_leao
	count = count + 1
print(count)