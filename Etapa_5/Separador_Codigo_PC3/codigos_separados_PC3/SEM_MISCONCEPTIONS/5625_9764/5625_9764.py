#preço
tap = 5.50
sal = 4.00
acai = 10.00

escolher = input("T ou S: ").upper()
qtds_item = int(input("quantidade: "))
qtds_acai = int(input("quantidade: "))

if escolher == "S":
	soma = (qtds_item * sal) + (qtds_acai * acai)
	print(round(soma, 2))
else: 
	soma = (qtds_item * tap) + (qtds_acai * acai)
	print(round(soma,2))