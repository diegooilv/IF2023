numero = int(input())

poks = []
pegos = 0

for i in range(numero):
    pokemon = input()
    if pokemon in poks:
        continue
    else:
        poks.append(pokemon)
        pegos += 1

print(f"Falta(m) {151 - pegos} pomekon(s).")
