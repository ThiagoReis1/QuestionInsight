n = int(input("Termos:"))
t = 1
s = 0

while(t<=n):
	s = s + (-1)**t * (t)**2 / (7+(2*t-1))
	t = t + 1
	
print(round(s,11))