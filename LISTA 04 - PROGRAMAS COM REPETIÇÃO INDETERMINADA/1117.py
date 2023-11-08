nota = []
while True:
    a = float(input())
    if a >= 0 and a <= 10:
        nota.append(a)
        if len(nota) == 2:
            break
    else:
        print('nota invalida')
media = 0
for y in nota:
    media += y
media = media/2
print(f'media = {media:.2f}')
