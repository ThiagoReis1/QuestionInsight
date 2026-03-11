altura_cicero = 1.8
taxa_cicero = 0.01
a = float(input())
t = float(input())

anos = 0
altura_cice = 1.8
altura_a = a

while altura_a<altura_cice:
	altura_cice = altura_cice+taxa_cicero
	altura_a = altura_a+t
	anos = anos+1
print(anos)