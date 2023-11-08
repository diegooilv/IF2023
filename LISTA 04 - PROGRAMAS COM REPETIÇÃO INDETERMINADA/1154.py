idades = 0
total = 0
controle = 0
while True:
    controle = int(input())
    if controle > 0:
        total += controle
        idades += 1
    else:
        break
print(f'{total/idades:.2f}')
