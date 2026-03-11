f1 = int(input("pontos de força iniciais do lobisomem:"))
lua = int(input("porcentual de lua visivel:"))
f2 = (f1 - 23 *(1-(lua/100)))
if (f2<0):
	print ("ATACO")
else:
	print ("CORRO")