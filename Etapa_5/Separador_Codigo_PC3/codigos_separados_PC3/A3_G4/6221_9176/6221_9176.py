x = int(input("Digite um numero para servir como base do intervalo: "))
y = int(input("Digite um numero que sirva como maximo do intervalo: "))
b = 0
cont = 0
while x <= y:
 if x % 7 == 0:
  b = b + x
 x += 1
print(b)