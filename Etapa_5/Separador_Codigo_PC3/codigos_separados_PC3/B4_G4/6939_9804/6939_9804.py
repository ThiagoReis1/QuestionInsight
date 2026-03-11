v = float(input())
c = input()

if c.upper() == "D":
	d = 0.19
	t = v - (v * d)
elif c.upper() == "P":
	d = 0.19
	t = v - (v * d)
else:
	o = int(input())
	if o == 1:
		d = 1
		t = v
	else:
		d = 0.09
		t = v + (v * d)


print(round(t,2))