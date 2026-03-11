tv = float(input("qual o tempo de voo: "))
v1 = float(5000)
v2 = 8000
p = float(100)
if (tv <= 200):
	custo = v1 + (p*tv)
elif (tv > 200):
	custo = (v2 + (p * 200) + (90 * (tv - 200)))
print(round(custo, 2))
	