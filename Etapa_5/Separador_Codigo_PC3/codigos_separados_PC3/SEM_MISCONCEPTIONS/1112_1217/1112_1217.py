a = float(input("Consumo de energia(kWh):"))
tipo = input("Tipo reais ou interios:")
print("Entradas:", a, "kWh e tipo", tipo)
if(tipo == "Reais"):
	if(a < 0):
		preco = -1
   elif(a >= 0 and a <= 800):
      preco = (a * 0.5) + a
elif(tipo == "inteiros"):
    if(a <= 0):
        preco = -1
   elif(a > 800 and a <= 1000):
else:
    preco = -1
  
if(preco == -1):
    print("Dados invalidos")
else:
    print("Novo salario: R$", round(preco, 2))
		