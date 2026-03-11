n = input("cara ou coroa: ")

t = 0
ca = 0

while n.upper() != "S":
	if n.upper() == "CARA" :
		ca = ca + 1
	n = input("cara ou coroa: ")
	t = t + 1
	por = 100*ca/t

print(t)
print(round(por,2))
