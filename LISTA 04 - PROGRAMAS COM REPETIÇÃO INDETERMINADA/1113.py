while True:
    x, y = map(int, input().split())
    if x != y:
        if x > y:
            print('Decrescente')
        elif x < y:
            print('Crescente')
    else:
        break
