qt = int(input("quantidade de combustivel: "))
msg = 0
if qt < 17.5:
	msg = qt + 1.5
elif qt < 35.0 and qt >= 17.5:
	msg = qt + 2.3
elif qt < 50.0 and qt >= 35.0:
	msg = qt + 3.3
else:
	msg = qt + 4.7
print(round(msg, 1))	