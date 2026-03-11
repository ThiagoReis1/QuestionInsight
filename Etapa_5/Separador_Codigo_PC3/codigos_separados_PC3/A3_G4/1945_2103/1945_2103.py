#ASPARTATO = C4H6NO4
#CISTEINA = C3H7NO2S

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

mol1 = input("Digite a molecula: ")
mol = mol1.lower()

if(mol == "aspartato"):
	num = c*4 + h*6 + n + o*4

if(mol == "cisteina"):
	num = c*3 + h*7 + n + o*2 + s
	
print(round(num,2))