largura = float(input("largura da fazenda"))
comprimento = float(input("comprimento da fazenda"))
custo = float(input("custo construcao da cerca"))

perimetro_paralelogramo = 2 * (largura + comprimento)

custo_total = (perimetro_paralelogramo * custo)

print (round(custo_total, 2))