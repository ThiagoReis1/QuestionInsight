cm = float(input())
if cm < 17.5:
	total = cm + 0.8
	print(round(total, 1))
if cm > 17.50 and cm < 35.0:
	total = cm + 1.3
	print(round(total, 1))
if cm > 35.0 and cm < 50:
	total = cm + 2.1
	print(round(total, 1))
if cm >= 50:
	total = cm + 3.0
	print(round(total, 1))