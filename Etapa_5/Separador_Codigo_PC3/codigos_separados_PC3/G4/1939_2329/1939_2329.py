n = input("nome do aa:")
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
pma = (4 * C) + (8 * H) + (2 * N) + (3 * O)
pmt = (11 * C) + (11 * H) + (2 * N) + (2 * O)
if (n.upper() == "ASPARAGINA"):
	print(round(pma,2))
else:
	print(round(pmt,2))