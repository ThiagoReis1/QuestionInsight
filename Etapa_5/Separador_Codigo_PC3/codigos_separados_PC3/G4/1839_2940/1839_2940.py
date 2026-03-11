## valores de entrada: pressao (p); número e mols (n);temperatura (t)

p = float(input('Insira um valor para a Pressão: '))
n = float(input('Insira um valor para o número de mols: '))
t = float(input('Insira um valor para a Temperatura: ')) + 273.15

## valor da constante universal
R = 0.082

## calculo para encontrar o volume V
V = ((n * R * t) / p)

## impressao do calculo do volume
print(V)

