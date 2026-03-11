t=int(input(""))
p=int(input(""))
taxat=float(input(""))
taxap=float(input(""))
nm=int(input(""))

soma = 0
i = 0
tt = taxat/100
tp = taxap/100
t1 = t + (t * tt)
t2 = p + (p * tp)

while (soma <= nm):
	soma = t1 + t2
	t1 = t1 + (t1 * tt)
	t2 = t2 + (t2 * tp)
	i = i + 1
print(i)