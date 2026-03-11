from numpy import*
s = array(eval(input('insira a seu codigo:')))
s_n =zeros(size(s), dtype=int)

for i in range(size(s)):
	if s[i] == 0 :
		s_n[i] = 9
	else:
		s_n[i] = s[i]**2
		
print(s_n)