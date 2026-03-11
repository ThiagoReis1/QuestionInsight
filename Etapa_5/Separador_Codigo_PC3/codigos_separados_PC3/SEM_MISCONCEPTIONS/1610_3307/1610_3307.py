from numpy import*

strin = input('No.: ')
vetstr = strin.split(',')

i = 0 # cont

while i < len(vetstr): 
	vetstr[i] = int(vetstr[i])
	i = i + 1
print(sum(vetstr))
	

