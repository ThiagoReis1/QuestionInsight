ap = float(input("altura: "))
tp = float(input("taxa: "))
aj = 1.77
tj = 0.02
c= 0
while ap < aj:
	c = c + 1
	ap = ap + tp
	aj = aj + tj
	
	
print(c)
	