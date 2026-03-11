from numpy import*

st = input().upper().split(',')
ax = zeros(4, dtype=int)

for i in range(len(st)):
	if st[i] == 'A':
		ax[0] = ax[0] + 1
	elif st[i] == 'B':
		ax[1] = ax[1] + 1
	elif st[i] == 'C':
		ax[2] = ax[2] + 1
	elif st[i] == 'D':
		ax[3] = ax[3] + 1
print(ax)