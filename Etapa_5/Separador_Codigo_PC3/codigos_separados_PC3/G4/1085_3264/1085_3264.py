n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

valor = (n1 + (n2 + n3) + (n4 + n5))/5

print(round(valor,2))

if(valor >= 6):
  print("Aprovacao")
else:
  print("Reprovacao")