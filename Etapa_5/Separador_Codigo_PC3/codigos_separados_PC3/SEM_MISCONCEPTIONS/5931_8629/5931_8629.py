preco = 45

minutos = float(input("minutos:"))
precominutos = 0.97 * minutos

plano = (preco + precominutos)
valor = (plano*42)/100 + plano
print(round(valor,2))