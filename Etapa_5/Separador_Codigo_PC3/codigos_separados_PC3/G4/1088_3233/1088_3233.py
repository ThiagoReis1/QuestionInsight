p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())

ma= (p1+p2+p3+p4+p5)/5
print(round(ma, 2))
if (ma>=7.0):
  print("Aprovacao")
else:
  print("Reprovacao por nota")