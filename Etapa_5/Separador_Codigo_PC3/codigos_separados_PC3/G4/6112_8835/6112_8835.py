qt = float(input("qtdd:"))
if qt < 17.5:
	cal = qt +10.5
	print(cal)
elif 17.5 == qt or qt < 35.0:
	cal = qt + 14.0
	print(cal)
elif 35.0 == qt or qt < 50:
	cal = qt + 18.6
	print(cal)
else:
	cal = qt + 24.5
	print(cal)