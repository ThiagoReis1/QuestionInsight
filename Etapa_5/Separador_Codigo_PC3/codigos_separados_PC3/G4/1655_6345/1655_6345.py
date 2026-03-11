from numpy import *

x = input("qtd estados: ").upper().split(',')
ac = 0
am = 0
pa = 0
ro = 0
rr = 0
i = 0

zero = zeros(5, dtype=int)

while i < len(x):
	if x[i] == 'AC':
		ac = ac + 1
		zero[0] = zero[0] + 1
	
	if x[i] == 'AM':
		am = am + 1
		zero[1] = zero[1] + 1
	
	if x[i] == 'PA':
		pa = pa + 1
		zero[2] = zero[2] + 1
		
	if x[i] == 'RO':
		ro = ro + 1
		zero[3] = zero[3] + 1
	
	if x[i] == 'RR':
		rr = rr + 1
		zero[4] = zero[4] + 1

	i = i + 1
	
print(max(zero))	
print(zero)