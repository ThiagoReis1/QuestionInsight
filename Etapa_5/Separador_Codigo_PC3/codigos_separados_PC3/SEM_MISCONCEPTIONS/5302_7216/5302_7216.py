massa = float(input())
anos = float(input())

while (anos>0):
	perda = massa*(5/100)
	massa = massa-perda
	anos = anos-1
	print(round(massa,2))