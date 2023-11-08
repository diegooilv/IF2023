a, b, c, d, e = input().split()
a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)
if a > b > c > d > e:
    print('D')
elif a < b < c < d < e:
    print('C')
else:
    print('N')
