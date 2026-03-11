h = int(input("quantos habitantes ?"))
v = int(input("quantos vampiros ?"))
x = int(input(" cada vampiro tranforma quantos habitantes por dia ?"))
y = int(input("matam quantos vampiros por dia ?"))
dias = 0
while(v <= h ):
	dias = dias + 1
	v = v*(1 + x) - y
	h = h - v*x + v
print(dias)
