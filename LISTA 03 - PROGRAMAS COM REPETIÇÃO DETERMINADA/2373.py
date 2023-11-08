copos_q = 0
bandejas = int(input())
for i in range(bandejas):
    latas, copos = map(int, input().split())
    if latas > copos:
        copos_q += copos
print(copos_q)
