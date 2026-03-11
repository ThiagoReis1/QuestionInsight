num = int(input("entre com um valor de 4 digitos:"))

pri = num//100
seg = num%100

d = (pri**2) + (seg**2)

if ( d == num):
	print("atende")
	print(num)
else:
	print("nao atende")
	print(num)