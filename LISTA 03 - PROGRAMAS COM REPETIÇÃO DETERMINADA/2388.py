valor = int(input())
total = 0
for a in range(0, valor):
    t, v = map(int,input().split())
    total += v*t
print(total)
