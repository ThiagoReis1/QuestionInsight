larguraf = float(input("Qual a largura da fazenda? "))
comprimentof = float(input("Qual o comprimento da fazenda? "))
custo_metro = float(input("Custo por metro? "))

custo_total = custo_metro * (2 * (larguraf + comprimentof))

print(round(custo_total,2))