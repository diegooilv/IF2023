itens = [4.00, 4.50, 5.00, 2.00, 1.50]
a, b = input().split()
a, b = int(a), int(b)
var = itens[a-1]*b
print(f'Total: R$ {var:.2f}')
