preço1=int(input('qualo primeiro preço'))
preço2=int(input('qualo primeiro preço'))
preço3=int(input('qualo primeiro preço'))
if preço1<preço2 and preço3:
    print('o mais barato e',preço1)
elif preço2>preço1 and preço3:
    print('o mais barato e',preço2)
elif preço3<preço1 and preço3:
    print('o mais barato e', preço3)