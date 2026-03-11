c = float(input("combustivel: "))

if c > 0 and c < 17.5:
	total = c + 10.5
elif c >= 15.5 and c < 35:
	total = c + 14.0
elif c >= 35 and c < 50:
	total = c + 18.6
elif c >= 50:
	total = c + 24.5
print(round(total, 1))