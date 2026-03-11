q = int(input("combustivel c: "))

if (0 < q < 17.5):
	t = q + 10.5
	print(t)
elif(17.5 <= q < 35.0):
	t = q + 14.0
	print(t)
elif (35<= q < 50.0):
   t = q + 18.6
   print(t)
else:
	t = q + 24.5
	print(t)