vetor = []

for i in range(10):
    numero = int(input())
    if numero > 0:
        vetor.append(numero)
    else:
        vetor.append(1)

for i in range(10):
    print(f"X[{i}] = {vetor[i]}")
