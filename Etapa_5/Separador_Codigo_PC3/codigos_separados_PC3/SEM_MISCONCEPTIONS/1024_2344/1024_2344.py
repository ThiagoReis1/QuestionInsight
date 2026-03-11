cA = float(input("Digite valor do comprimento A:"))
cB = float(input("Digite valor do comprimento B:"))
cC = float(input("Digite valor do comprimento C:"))
custo = float(input("Digite valor do custo por metro:"))

perimetro = (cA + cB + cC)
custo_total = perimetro * custo

print(round(custo_total, 2))

