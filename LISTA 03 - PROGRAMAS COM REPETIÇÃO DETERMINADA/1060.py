v1, v2, v3, v4, v5, v6 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
lista = [v1, v2, v3, v4, v5, v6]
valor = 0
for a in lista:
    if a > 0:
        valor += 1
print(f'{valor} valores positivos')
