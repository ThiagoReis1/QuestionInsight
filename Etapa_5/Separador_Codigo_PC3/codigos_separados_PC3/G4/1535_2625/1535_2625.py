x = float(input(" "))
k = int(input(" "))

arctgx = 0
num = 1
y = 0
while(y<k):
	n = ((x**num)*(-1)**y)/num
	arctgx = arctgx + n
	num = num + 2
	y = y + 1
print(round(arctgx,6))







