from math import*

veneno = float(input("Quantidade de veneno injetado: "))

casca_de_colmeia = (veneno/5)*(sqrt(9/5))
alho = (veneno**2)/pi
oleo_de_troll = sqrt(5*veneno/3)

print(round(casca_de_colmeia,2))
print(round(alho,2))
print(round(oleo_de_troll,2))