mA = int(input("Massa caminhão A em kg: "))
mB = int(input("Massa caminhão B em kg: "))
V0 = int(input("Velocidade caminhão B: "))

vf = (((2 * mA) + mB) / (mA + mB)) * V0
print(float(vf))