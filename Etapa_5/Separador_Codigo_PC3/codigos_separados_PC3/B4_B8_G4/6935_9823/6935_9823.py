vc = float(input())
cp = input().upper()

if cp == 'C':
	q = int(input())
	if q == 1:
		print(round(vc,2))
	elif q == 2:
		vf = vc + (vc*(7/100))
		print(round(vf,2))
elif cp == 'P':
	vf = vc - (vc*(12/100))
	print(round(vf,2))
else:
	vf = vc - (vc*(12/100))
	print(round(vf,2))