alt_p = float(input("altara da pessoa: "))
tax_p = float(input("taxa de cresc. da pessoa: "))
alt_c = 1.8
tax_c = 0.01
cont = 0

while(alt_p < alt_c):
	alt_p = alt_p + tax_p
	alt_c = alt_c + tax_c
	cont = cont + 1
print(cont)