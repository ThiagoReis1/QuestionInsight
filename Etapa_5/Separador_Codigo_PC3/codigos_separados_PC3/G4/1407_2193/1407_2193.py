pontos = int(input(""))
s1 = int(input(""))
s2 = int(input(""))
s3 = int(input(""))
N = s1 + s2 + s3
perde = 10 * N
M = (pontos - perde)
if ( M > 0):
	print(M)
	print("VIVO")
else:
	print("0")
	print("MORTO")