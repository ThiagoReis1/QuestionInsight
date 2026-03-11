from numpy import *
# Cria o vetor de 4 categorias com zeros
cont = zeros(5, dtype=int)
# Leitura do vetor de tipos sanguineos
vet = input("ESTADOS: ").upper().split(',')
# Contagem de ocorrencias
for x in vet:
   if (x == 'AM'):
      cont[0] = cont[0] + 1
   elif (x == 'PE'):
      cont[1] = cont[1] + 1
   elif (x == 'MG'):
      cont[2] = cont[2] + 1
   elif (x == 'SP'):
      cont[3] = cont[3] + 1
   elif (x == 'RS'):
      cont[4] = cont[4] + 1
print(max(cont))
print(cont)
