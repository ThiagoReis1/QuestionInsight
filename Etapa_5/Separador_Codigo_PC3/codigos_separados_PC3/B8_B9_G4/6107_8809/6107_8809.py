c=float(input("quantidade de combustiveis: "))
if c < 17.5:
	t=c+1.5
elif c >= 17.5 and c < 35:
	t=c+2.3
elif c >= 35 and c < 50:
	t=c+3.3
elif c >= 50:
	t=c+4.7
print(t)