x = int(input("valor x: "))
y = int(input("valor y: "))

acl = x
b = 0
while (acl <= y):
	if (acl % 2 == 0):
		b = b + acl
	acl = acl + 1
print(b)