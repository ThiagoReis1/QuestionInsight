import numpy as np

entrada = input()

palavra = entrada.split(',')
naciona = [0] * 5
for i in range(len(palavra)):
	if palavra[i] == 'AR':
		naciona[0] +=1
	elif palavra[i] == 'BR':
		naciona[1] +=1
	elif palavra[i] == 'CL':
		naciona[2] +=1
	elif palavra[i] == 'CO':
		naciona[3] +=1
	elif palavra[i] == 'UY':
		naciona[4] +=1
print(max(naciona))		
print(np.array(naciona))