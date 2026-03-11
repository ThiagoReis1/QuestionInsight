from numpy import *

doces = 2.25
d_count = 0

salgados = 4
s_count = 0

integrais = 6.9
i_count = 0

string = input("Digite a sequencia de compra: ").upper()

i = 0
contar = 1

tam = len(string)

while i < tam:
 if string[i] == "D":
  d_count += 1
 elif string[i] == "S":
  s_count += 1
 elif string[i] == "I":
  i_count += 1
 i += 1
 contar += 1

total = ((doces * d_count) + (salgados * s_count) + (integrais * i_count))

print(round(total, 2))