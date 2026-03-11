altura_luna = 1.65
taxa_luna = 0.02
cont = 0
alt_p= float(input())
taxa_p= float(input())

while altura_luna > alt_p:
	altura_luna= altura_luna + taxa_luna
	alt_p= alt_p + taxa_p
	cont += 1
print(cont)