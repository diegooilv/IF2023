salario = float(input())
if salario > 0 and salario <=400:
    perc = 15
elif salario > 400 and salario <= 800:
    perc = 12
elif salario > 800 and salario <= 1200:
    perc = 10
elif salario > 1200 and salario <= 2000:
    perc = 7
elif salario > 2000:
    perc = 4
novo_salario = salario + ((salario/100) * perc)
reajuste_ganho = (salario/100) * perc
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste_ganho:.2f}")
print(f"Em percentual: {perc} %")
