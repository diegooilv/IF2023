a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
p = int((a+b+abs(a-b))/2)
p = int((p+c+abs(p-c))/2)
print(f'{p} eh o maior')