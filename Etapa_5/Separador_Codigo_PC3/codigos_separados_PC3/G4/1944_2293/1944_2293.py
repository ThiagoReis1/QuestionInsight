A = input("qual aminoacido? ")
if (A.lower() == 'leucina'):
	mgm = round((12.011 * 6) + (1.0079 * 13) + 14.00674 +  (15.9994 * 2), 2)
else:
	mgm = round((6 * 12.011) + (15 * 1.0079) + (2 * 14.00674) + (15.9994 * 2), 2)
print(mgm)