ts = input("t/s: ")
qts = int(input("quantidade: "))
qa = int(input("acai: "))

t = qts * 5.50
s = qts * 4
a = qa * 10
if (ts.upper() == "T"):
	total = t + a
else:
	total = s + a
	
print(total)