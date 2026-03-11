a = int(input("d"))
b = input("a ou b").upper()
t = 2023 - a
o = t - 18
m = t - 17
l = -t +17
k = -t +18
if b == "I" and t>=17:
	print("sim")
	print(m)
elif b == "B" and t>=18:
	print("sim")
	print(o)
elif b == "B" and	t<18:
	print("nao")
	print(k)
elif b == "I" and t<17:
	print("nao")
	print(l)
else:
	print("invalido")