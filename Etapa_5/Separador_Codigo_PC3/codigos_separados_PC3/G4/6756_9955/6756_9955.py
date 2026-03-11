dr=int(input())
cd=175.00

if dr<15:
	tx=20.00
elif dr==15:
	tx=16.00
else:
	tx=10.00

total=(cd*dr)+tx
print(round(total,2))