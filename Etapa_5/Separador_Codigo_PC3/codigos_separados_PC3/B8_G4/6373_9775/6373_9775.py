from numpy import *
work = input().upper().split(',')
end = zeros(4, dtype = int)
for i in range(len(work)):
	if work[i] == 'A':
		end[0] += 1
	elif work[i] == 'P':
		end[1] += 1
	elif work[i] == 'D':
		end[2] += 1
	elif work[i] == 'M':
		end[3] += 1
print(end)