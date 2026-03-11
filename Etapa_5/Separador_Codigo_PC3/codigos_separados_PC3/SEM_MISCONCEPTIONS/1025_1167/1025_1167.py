largura = float(input("largura da fazenda "))
comprimento = float(input("comprimento da fazenda "))
custo = float(input("valor da construcao por m "))
perimetro = 2 * (largura + comprimento)
valortotal = perimetro * custo
print(round(valortotal, 2))