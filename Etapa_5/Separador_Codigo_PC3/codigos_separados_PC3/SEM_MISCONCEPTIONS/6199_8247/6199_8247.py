altura_cicero = 1.8
taxa_cicero = 0.01
h = float(input())
tc = float(input())
c = 0
while h < altura_cicero:
	altura_cicero = altura_cicero + taxa_cicero
	h = h + tc
	c = c + 1
print(c)