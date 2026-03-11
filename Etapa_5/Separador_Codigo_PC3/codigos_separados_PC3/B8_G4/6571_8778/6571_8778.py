peso = float(input())
tf = 10
a = tf + 3.75
b = tf + 4.75
c = tf + 5.75

if peso < 5:
	print("total=",round(a, 2))
elif peso == 5:
	print("total=",round(b, 2))
elif peso > 5:
	print("total=",round(c, 2))
