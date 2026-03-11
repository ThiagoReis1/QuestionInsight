from numpy import*

v = array(eval(input("")))

p = min(v)

m = ((sum(v) - p)/3)

print(round(m,2))

if (m>=5):
	print("APROVOU")
else:
	print("REPROVOU")
