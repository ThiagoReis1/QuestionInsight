p = float(input("O peso do saco de racao em gramas: "))
q = float(input("A quantidade diaria de racao em gramas: "))

qr = q * 7
qrs = p - qr

print(round(qrs, 4))