raio = float(input("Informe o valor do raio, em metros, da fazenda: "))
custo = float(input("Informe o valor do custo, por metro quadrado, da aplicação do fertilizante: "))
import math
area = ((math.pi) * (raio**2))
custo_total = (area * custo)
custo_total2 = round(custo_total,2)
print (custo_total2)
