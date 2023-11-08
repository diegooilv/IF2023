def quadrante(x,y):
    if x > 0 and y > 0:
        return 'primeiro'
    elif x > 0 and y < 0:
        return 'quarto'
    elif x < 0 and y > 0:
        return 'segundo'
    elif x < 0 and y < 0:
        return 'terceiro'

while True:
    v1, v2 = map(int, input().split())
    if v1 != 0 and v2 != 0:
        print(quadrante(v1,v2))
    else:
        break
