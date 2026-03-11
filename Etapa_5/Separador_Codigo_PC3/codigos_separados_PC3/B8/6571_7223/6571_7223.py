# faça seu código aqui!
Custo_Fixo = 10
Peso = float(input("Peso em Kg: "))

if float(Peso<5):
	T=3.75
elif float(Peso==5):
	T=4.75
elif float(Peso>5):
	T=5.75
Total=Custo_Fixo+T
print("total=",round(Total,2))
