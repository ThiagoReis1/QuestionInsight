import math

# faça seu código aqui!

comprimento_do_lado_do_hexagono = float(input("Informe o comprimento do lado do hexagono: "))

apotema = comprimento_do_lado_do_hexagono / (2 * math.tan(math.pi/6))

area_do_hexagono = 3 * comprimento_do_lado_do_hexagono * apotema

print(round(area_do_hexagono, 2))