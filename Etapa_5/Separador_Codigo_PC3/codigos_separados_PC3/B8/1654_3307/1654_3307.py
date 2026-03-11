from numpy import*

strin = input('Estados: ').split(',')
strin_out = zeros(5,dtype=int)

for i in strin: 
	if i.upper() == 'AM':
		strin_out[0]+=1
	elif i.upper() == 'PE':
		strin_out[1]+=1
	elif i.upper() == 'MG':
		strin_out[2]+=1
	elif i.upper() == 'SP':
		strin_out[3]+=1
	elif i.upper() == 'RS':
		strin_out[4]+=1

print(max(strin_out))
print(strin_out)