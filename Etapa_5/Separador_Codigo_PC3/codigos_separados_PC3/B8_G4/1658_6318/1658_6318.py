from numpy import*
st = array(input("origem:: ").upper().split(','))

a = zeros(5, dtype = int)

for i in range(size(st)):
	if st[i] == "CHN":
		a[0] = a[0] + 1
	elif st[i]  == "JPN":
		a[1] = a[1] + 1
	elif st[i] == "KOR":
		a[2]  = a[2] + 1
	elif st[i] == "MGL":
		a[3] = a[3] + 1
	elif st[i] == "THA":
		a[4] = a[4] + 1
print(max(a))
print(a)
	
	