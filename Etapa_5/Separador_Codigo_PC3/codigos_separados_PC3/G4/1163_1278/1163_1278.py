l = int(input("lambaris:"))
t = int(input("tucunare:"))
lt = float(input("taxa de crescimento lambari:"))
tt = float(input("taxa de crescimento tucunare:"))
i = 1
while (l>=t):
	l = l + l*lt-t*2
	t = t + t*tt
	i = i + 1

print(i)
