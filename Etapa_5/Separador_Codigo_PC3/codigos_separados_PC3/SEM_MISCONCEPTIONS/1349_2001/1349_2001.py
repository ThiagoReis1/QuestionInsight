from math import *

num_arvores = float(input("Digite a estimativa de arvores por m2: "))
lado_do_pentagono = float(input("Digite o lado do pentagono da regiao em m: "))

area = (lado_do_pentagono**2)*(sqrt((25 + 10*(sqrt(5)))))/4

estimativas = area * num_arvores

print (int(estimativas))