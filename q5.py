n1=int(input('sua primeira nota'))
n2=int(input('sua segunda nota '))
n3=(n1+n2/2)
if n3<=7:
    print(' parabens,aprovado')
elif n3<=10:
    print('aprovado com disniçao')
else:
    print('vc foi reprovado')