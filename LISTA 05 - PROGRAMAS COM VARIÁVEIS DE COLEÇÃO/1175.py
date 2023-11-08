vetor = []

for i in range(20):
    valor = int(input())
    vetor.append(valor)

for i in range(10):
    temp = vetor[i]
    vetor[i] = vetor[19 - i]
    vetor[19 - i] = temp

for i in range(20):
    print(f"N[{i}] = {vetor[i]}")
