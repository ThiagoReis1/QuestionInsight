n1 = float(input())
n2 = float(input())
n3 = float(input())
media = (n1 + n2 + n3)/3

print(round(media, 2))

if(media < 6):
	print("Reprovacao")
else:
	print("Aprovacao")
