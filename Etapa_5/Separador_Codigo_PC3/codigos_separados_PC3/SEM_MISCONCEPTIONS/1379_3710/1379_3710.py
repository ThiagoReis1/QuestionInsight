# triângulo retangulo
# est = quantidade de carro / area

est = float(input("Insira a estimativa de carros: "))
cateto_a = float(input("Insira o comprimento do primeiro cateto: "))
cateto_b = float(input("Insira o comprimento do segundo cateto: "))

area = (cateto_a * cateto_b) // 2

qtd_car = est * area

print(int(qtd_car))