nt1 = int(input("Numero inicial de tambaquis:"))
np1 = int(input("Numero inicial de pacus:"))
tt = int(input("Taxa de crescimento de tambaquis:"))
tp = int(input("Taxa de crescimento de pacus:"))
nmax = int(input("Numero maximo de especies:"))

i = 0
somat = nt1
somap = np1
somatp = somat + somap
t = nt1 * tt / 100
p = np1 * tp / 100

while (somatp <= nmax):
	i = i+1
	somat = somat + t
	somap = somap + p
	somatp = somat +somap
	t = somat* tt / 100
	p = somap*tp/100
print(i)