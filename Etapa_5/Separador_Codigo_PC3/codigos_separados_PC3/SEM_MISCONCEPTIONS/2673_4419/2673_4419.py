import math

raio = float(input("Qual a medida do raio do poligono: "))
qtdLados = int(input("Qunatos lados ha no poligono: "))

medidaLado = 2 * raio * math.sin(math.pi/qtdLados)
print(round(medidaLado,2))