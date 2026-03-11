i = int(input("idade: "))
m = 0
t = 0
while(i != -1):
	if(i < 18):
		m = m + 1
	else:
		m = m
	i = int(input("idade: "))
	t = t + 1

print(t)
print(round((100 * m) / t, 2))