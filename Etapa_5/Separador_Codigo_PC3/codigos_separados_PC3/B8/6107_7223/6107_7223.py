Combustivel_Comum = float(input("Combustivel em Kl: "))
#2,3
#3,3
#4,7
if 0<Combustivel_Comum<17.5:
	Coaxium = 1.5
elif 17.5<=Combustivel_Comum<35:
	Coaxium = 2.3
elif 35<=Combustivel_Comum<50:
	Coaxium = 3.3
elif Combustivel_Comum>=50:
	Coaxium = 4.7

Total = Combustivel_Comum + Coaxium
print(round(Total,1))