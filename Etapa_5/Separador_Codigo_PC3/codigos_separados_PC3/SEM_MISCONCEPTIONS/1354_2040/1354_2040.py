# Teste de Irene Andrea 
from math import*

potencia_media_desejada = float(input("Digite a potencia desejada em watt/m2: "))
raio_comodo = float(input("Digite o raio do comodo em metros: "))

area = pi * raio_comodo ** 2

potencia_total = area * potencia_media_desejada

print(round(potencia_total, 2))
