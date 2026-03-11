est_de_carro = float(input("carro: "))
base_maior = float(input("base maior: "))
base_menor = float(input("base menor: "))
altura = float(input("altura: "))

carros = (base_maior + base_menor) * altura / 2

estimativa = carros * est_de_carro

print(int(estimativa))
