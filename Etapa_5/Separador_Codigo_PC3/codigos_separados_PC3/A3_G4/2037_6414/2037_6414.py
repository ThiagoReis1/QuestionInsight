i = int(input("idade: "))
a = 0
f = i

while (f != -1):
	f = int(input("idade: "))
	if (i<18):
		a = a + 1
	else:
		a = 0
		f = int(input("idade: "))
print(a)