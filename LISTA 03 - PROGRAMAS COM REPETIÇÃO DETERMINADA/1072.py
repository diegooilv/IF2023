im, out = 0, 0
n = int(input())
for i in range(n): 
    m = int(input())
    if m >= 10 and m <= 20:
        im += 1
    else: 
        out += 1
print(f'{im} in\n{out} out')
