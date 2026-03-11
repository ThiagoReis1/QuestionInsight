valor = int (input ("valor: "))

v6 = valor // 100000
sobra6 = valor%100000

v5 = sobra6 // 10000
sobra5 = sobra6%10000

v4 = sobra5 // 1000
sobra4 = sobra5%1000


v3 = sobra4 // 100
sobra3 = sobra4%100

v2 = sobra3 // 10
sobra2 = sobra3%10

v1 = sobra2 // 1

eq1 = v6*100 + v5*10 +v4
eq2 = v3*100 + v2*10 +v1

if (eq1 - eq2)**4 == valor:
	print (valor,"atende a propriedade")
else:
	print ((eq1 - eq2)**4)


