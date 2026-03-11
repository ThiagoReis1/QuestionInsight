# faça seu código aqui!
custo = 50
dist = int(input())

if dist < 10:
	v = custo + 5.50
	print("total=", round(v , 2))
elif dist == 10:
	v = custo + 7.75
	print("total=", round(v , 2))
elif dist > 10: 
	v = custo + 10.0
	print("total=", round(v , 2))