x = float(input())

var = 0
if -1 >= x or 1 <= x:
	var = x ** 2
elif -1 < x < 0 or 0 < x < 1:
	var = x
elif x == 0:
	var = 1
print(round(var, 4))