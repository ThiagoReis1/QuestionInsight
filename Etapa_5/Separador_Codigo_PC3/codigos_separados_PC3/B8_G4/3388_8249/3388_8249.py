bw = (input())
vm = float(input())

if bw == "B":
	cal = vm / 3.41214
elif bw == "W":
	cal = vm * 3.41214
	
print(round(cal, 2))
