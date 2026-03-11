from numpy import*
vet =  input("vet: ").split(',')

BE = 0
ES = 0
FR = 0
IT = 0
PT = 0

for i in range (len(vet)):
	if(vet[i] == "BE"):
		BE =  BE +1
	if (vet[i] == "ES"):
		ES = ES +1
	if (vet[i] == "FR"):
		FR = FR +1
	if(vet[i] == "IT"):
		IT = IT +1
	if(vet[i] == "PT"):
		PT = PT +1
	
s = zeros(5, dtype= int)

for i in range(size(s)):
	s[0]= BE
	s[1]= ES
	s[2]= FR
	s[3]= IT
	s[4]= PT
	
print(max(ES,FR,PT,ES,BE,IT))
print(s)