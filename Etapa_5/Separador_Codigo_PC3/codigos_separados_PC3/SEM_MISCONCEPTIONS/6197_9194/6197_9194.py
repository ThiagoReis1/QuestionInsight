altura_a = 1.6
taxa_a = 0.02
altura_b= float(input('inserir alt:'))
taxa_b= float(input('inserir taxa:'))
t= 0

while altura_a>altura_b:
	altura_b = altura_b + taxa_b
	altura_a= altura_a + taxa_a
	t += 1
print(t)
		