s = input('Digite (I) para iogurtes, (M) para massas ou (S) para salgadinhos: ')

total = 0
cont_i=0
cont_m=0
cont_s=0
i=0

while i < len(s):
	if s[i] == 'I':
		cont_i = cont_i + 3.75
		i+=1
	elif s[i] == 'M':
		cont_m = cont_m + 4.50
		i+=1
	elif s[i] == 'S':
		cont_s = cont_s + 2.90
		i+=1
total = cont_i+cont_m+cont_s		
print(round(total,2))
	
	
	
	



