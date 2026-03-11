# faça seu código aqui!
dist = int(input())
custo = 50.0
if(dist < 10):
	custo += 5.5
elif(dist == 10):
	custo += 7.75
else:
	custo += 10
print(round(custo,2))