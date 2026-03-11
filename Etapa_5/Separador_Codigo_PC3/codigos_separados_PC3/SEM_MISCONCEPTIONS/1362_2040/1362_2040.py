from math import*

a = float(input("Digite gramas de veneno injetado: "))

casca_colmeia = a/5 * (9/5)** 0.5

gr_alho = a**2 / pi

gr_troll = (5 * a / 3)** 0.5

print(round(casca_colmeia, 2))
print(round(gr_alho, 2))
print(round(gr_troll, 2))

