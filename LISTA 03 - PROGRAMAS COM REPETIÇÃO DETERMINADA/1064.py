valores_positivos = 0
total = 0
for i in range(6):
    num = float(input())
    if num > 0:
        total += num
        valores_positivos += 1
print(f'{valores_positivos} valores positivos\n{total/valores_positivos:.1f}')
