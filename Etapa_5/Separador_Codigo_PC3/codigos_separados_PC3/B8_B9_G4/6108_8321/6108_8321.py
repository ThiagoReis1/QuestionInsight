m = float(input("quantidade de combustivel"))

if (m < 17.5):
	k = (m + 1.5)
elif ( m >= 17.5 and m < 35):
	k = (m + 2.3)
elif ( m >= 35 and m < 50):
	k = (m + 3.3)
elif (m >= 50):
	k = m + 4.7
print(round(k,1))