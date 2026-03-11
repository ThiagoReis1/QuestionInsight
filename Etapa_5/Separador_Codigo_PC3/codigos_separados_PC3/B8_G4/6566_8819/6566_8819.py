qp = int(input())

if (qp < 10):
	t = 30. + 3.25
	print("total=", round(t, 2))
elif (qp == 10):
	t = 30. + 4.50
	print("total=", round(t, 2))
elif (qp > 10):
	t = 30. + 6.
	print("total=", round(t, 2))