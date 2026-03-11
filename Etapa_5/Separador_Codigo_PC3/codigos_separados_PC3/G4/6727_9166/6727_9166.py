X = int(input(""))

if (X % 31 == 0):
	print("{}\nsim".format(X//31))
else:
	print("{}\nnao".format(X%31))