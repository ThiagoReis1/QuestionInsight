aj = 1.77
tj = 0.02
ap = float(input("altura: "))
tp = float(input("taxa: "))
anos = 0
while ap < aj:
	aj = aj + tj
	ap = ap + tp
	anos = anos + 1
print(anos)