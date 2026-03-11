altura_macaco = 1.4
taxa_macaco = 0.06
alt_leao = float(input("altura:"))
tax_leao = float(input("taxa:"))
anos = 0
while altura_macaco < alt_leao:
	anos = anos+1
	altura_macaco = altura_macaco + taxa_macaco
	alt_leao = alt_leao + tax_leao
print(anos)

