pesq = input('qual opiniao(OUT): ').upper()
cont_S = 0
cont_I = 0
cont_N = 0
while pesq != 'X':
  if pesq == 'S':
    cont_S += 1
  elif pesq == 'I':
    cont_I += 1
  elif pesq == 'N':
    cont_N += 1
  pesq = input('qual opiniao(IN): ').upper()
print(cont_S)