from numpy import *

e = array(eval(input("energia: ")))
total = 0

if e > 0 and e <= 150:
	total = e * 0.60 + 5.00
elif e > 150 and e <= 250:
	total = e * 0.65 + 8.00
elif e > 250 and e <= 350:
	total = e * 0.70 + 12.00
else:
	total = e * 0.75 + 16.00

print(round(total, 2))
	