X = int(input("Insira um número X:"))
Y = int(input("Insira um número Y:"))
M = int(input("Insira um número M:"))

for x in range(0,M):
    xi = int(input("\nQual a largura da peça:"))
    yi = int(input("\nQual a altura da peça:"))

    if xi > x:
        print("Não")
    elif yi > y:
        print("Não")
    else:
        print("Sim")