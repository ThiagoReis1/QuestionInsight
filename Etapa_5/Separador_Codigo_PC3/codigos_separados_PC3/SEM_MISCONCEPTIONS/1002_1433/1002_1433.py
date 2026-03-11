from math import *
raio_fazenda = float(input("Tamanho da fazenda: ")) 
preco = float(input("Qual o preco? ")) 
total = preco * raio_fazenda**2 * pi
print(round(total, 2))