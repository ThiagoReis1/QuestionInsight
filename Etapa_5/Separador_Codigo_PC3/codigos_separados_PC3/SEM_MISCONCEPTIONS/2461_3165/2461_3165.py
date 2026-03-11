Preco = float(round(input("Informe o preco de custo: ")/2)
if(Preco<="50.00"):
	Lucro = 100
elif(Preco>="50.01", Preco<="100.00"):
	Lucro = 50
elif(Preco>="100.01" or Preco<="500.00"):
	Lucro = 40
elif(Preco>="500.00"):
	Lucro = 30
Vfv = Preco + Lucro
print("Vfv")