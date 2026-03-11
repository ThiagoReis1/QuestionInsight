from numpy import*
a = array(eval(input("numeros gerados pelo dado: ")))
i = 0
ac = 0
while i < size(a):
	if  a[i] == 1:
		ac = ac + 10
	elif a[i] == 2:
		ac = ac + 5
	elif a[i] == 3:
		ac = ac + 10
	elif a[i] == 4:
		ac = ac + 5
	elif a[i] == 5:
		ac = ac + 10
	elif a[i] == 6:
		ac = ac + 5
	i = i + 1
print(ac)
