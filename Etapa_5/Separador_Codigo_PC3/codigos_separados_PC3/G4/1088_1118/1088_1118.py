p1=float(input())
p2=float(input())
p3=float(input())
p4=float(input())
p5=float(input())

media = (p1+p2+p3+p4+p5)/5

print(round(media,2))
if media >= 7:
	print("Aprovacao")
else:
	print("Reprovacao")