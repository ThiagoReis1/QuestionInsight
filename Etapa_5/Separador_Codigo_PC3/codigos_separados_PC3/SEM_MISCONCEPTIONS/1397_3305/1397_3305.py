#empresa agricola Agro Fertil
area = int(input("entre com a quantidade de hectares: "))
if(area <= 10000):
	custo = 5*area
else:
	exc=area-10000
	custo= (10000*5.00)+(exc*4.00)
print(round(custo,2))
