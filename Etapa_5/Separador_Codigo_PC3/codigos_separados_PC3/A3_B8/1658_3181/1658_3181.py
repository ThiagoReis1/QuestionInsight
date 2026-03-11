from numpy import*
x = input("").upper().split(',')
quantidade = 0
quant_chn = 0
quant_jpn = 0
quant_kor = 0
quant_mgl = 0
quant_tha = 0
res = zeros(5, dtype=int)
for i in range(size(x)):
	if(x[i] == 'JPN'):
		quant_jpn+=1
	elif(x[i] == 'CHN'):
		quant_chn+=1
	elif(x[i] == 'KOR'):
		quant_kor+=1
	elif(x[i] == 'MGL'):
		quant_mgl+=1
	elif(x[i] == 'THA'):
		quant_tha+=1

for k in range(size(x)):
	if(k == 0):
		res[0] = quant_chn
	elif(k == 1):
		res[1] = quant_jpn
	elif(k == 2):
		res[2] = quant_kor
	elif(k == 3):
		res[3] = quant_mgl
	elif(k == 4):
		res[4] = quant_tha
r = max(res)
print(r)
print(res)