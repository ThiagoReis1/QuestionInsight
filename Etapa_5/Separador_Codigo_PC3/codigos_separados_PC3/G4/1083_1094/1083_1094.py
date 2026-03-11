p1=float(input())
p2=float(input())
p3=float(input())
media= (p1+p2+p3)/3
if(media>=6):
  print(round(media,2),"Aprovacao")
else:
  print(round(media,2),"Reprovacao")