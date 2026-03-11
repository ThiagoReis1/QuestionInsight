q = int(input("abra: "))

if(0 < q < 17.5):
	t = q + 0.8
	print(t)
elif(17.5 <= q < 35.0):
	t = q + 1.3
	print(t)
elif(35.0 <= q < 50.0):
	t = q + 2.1
	print(t)
else:
	t = q + 3.0
	print(t)