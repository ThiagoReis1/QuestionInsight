
am= input("aminoacido: ")

if  ( am.lower() == "histidina"):
	s= (12.011 * 6) + (1.00794 * 10) + (14.00674 * 3) + (15.999 * 2)
if  ( am.lower() == "prolina"):
	s= (12.011 * 5) + (1.00794 * 10) + (14.00674) + (15.999 * 2)

print(round(s,2))