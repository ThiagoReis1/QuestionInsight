from numpy import*
st = input("produtos comprados: ").upper()

i = 0
ach = 0
acl = 0
ace = 0
total = 0

while i < len(st):
	
	if st[i] == "H":
		ach = ach + 1
		total = total + 3.85
	elif st[i] == "L":
		acl = acl + 1
		total = total + 2.95
	elif st[i] == "E":
		ace = ace + 1
		total = total + 7.90
	i = i + 1
print(round(total,2),ach,acl,ace)