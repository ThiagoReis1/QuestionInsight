X= input("T ou P ")
Q= int(input("quantidade de fatias"))
C = int(input("quantidade de capuccinos "))

if X == "T":
	valor= Q*6+4.50*C
	print(valor)
if X == "P":
	valor= Q*5+4.50*C
	print(valor)

	

