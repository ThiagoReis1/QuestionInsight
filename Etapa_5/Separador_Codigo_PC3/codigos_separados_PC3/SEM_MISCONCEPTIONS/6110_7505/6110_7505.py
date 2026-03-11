combus = float(input())

if combus > 0 and combus < 17.5:
	calc = combus + 10.5
elif combus > 17.5 and combus < 35:
	calc = combus + 14
elif combus > 35 and combus < 50:
	calc = combus + 18.6
else:
	calc = combus + 24.5
print(calc)