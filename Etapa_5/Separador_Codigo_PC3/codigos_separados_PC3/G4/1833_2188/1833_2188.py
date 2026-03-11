ma = int(input("Massa do caminhao A:"))
mb = int(input("Massa do caminhao B:"))
vo = int(input("Velocidade do caminhao B em m/s:"))

vf = (((2 * ma) + mb) / (ma + mb)) * vo

print(float(vf))