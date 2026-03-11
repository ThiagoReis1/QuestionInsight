p1 = round(float(input()),2)
p2 = round(float(input()),2)
p3 = round(float(input()),2)
p4 = round(float(input()),2)

media = (p1+p2+p3+p4)/ 4

print(round(media,2))

if (media >= 5): 
	print("Aprovacao")
else:
	print("Reprovacao")