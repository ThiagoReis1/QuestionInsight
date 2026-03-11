# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo
# Curso: Estatistica

from math import pi, sin

# Inputs ( raio r, numero de lados n )
raio_r = float(input('Digite o raio r: '))
lados_n = int(input('Digite o numero de lados do poligono: '))

# Calculando o lado L
calculo_lado = 2 * raio_r * sin(pi/lados_n)

# Output ( lado L com duas casas decimais)
print(round(calculo_lado, 2))