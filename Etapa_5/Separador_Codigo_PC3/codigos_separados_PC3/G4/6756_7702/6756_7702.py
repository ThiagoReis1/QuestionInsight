d = int(input("dias: "))

if d == 15:
	t = d*175 + 16
elif d < 15:
	t = d*175 + 20
else:
	t = d*175 + 10
print(round(t,2))
	