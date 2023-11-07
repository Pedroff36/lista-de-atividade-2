salario_anterio=float(input('digite seu salario'))
salario_atual=0.0
diferença_entre_salarios=0.0
percentual_de_aumento=0.0
if salario_anterio<=288:
    percentual_de_aumento=20
elif salario_anterio<=750:
    percentual_de_aumento=15
elif salario_anterio<=1500:
    percentual_de_aumento=10
else:
    percentual_de_aumento=5

diferença_entre_salarios=salario_anterio*(percentual_de_aumento/100)
salario_atual=salario_anterio+diferença_entre_salarios
print(f'seu salario antes do reajuste era de {percentual_de_aumento:.2f}')
print(f'seu salario foi almentado em {percentual_de_aumento}%')
print(f'seu salario foi almentado em {diferença_entre_salarios:.2f}')
print(f'seu salario atual e de {salario_atual:.2f}')
    
