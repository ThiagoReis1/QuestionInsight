from numpy import*

vet = array(eval(input()))

i = 0
pts = 10000
while(i < size(vet)):
	if(vet[i] == 1):
		pts = pts * 2
	if(vet[i] == 2):
		pts = pts
	if(vet[i] == 3):
		pts = pts / 2
	if(vet[i] == 4):
		pts = pts / 4
	i = i + 1
print(round(pts, 2))