a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

delta = b**2-4*a*c
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    x1 = -b+(delta**(1/2))
    x1 = x1/(2*a)
    x2 = -b-(delta**(1/2))
    x2 = x2/(2*a)
    print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')
