cod1, pr1, qnt1 = input().split()
cod2, pr2, qnt2 = input().split()
print(f"VALOR A PAGAR: R$ {(float(pr1)*float(qnt1))+(float(pr2)*float(qnt2)):.2f}")
