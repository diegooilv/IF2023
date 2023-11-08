lista = input()
lista = lista.split()
letra = 'S'
for i in range(0, len(lista)):
    lista[i] = int(lista[i])
for i in lista:
    if i == 9:
        letra = 'F'
        break
print(letra)
