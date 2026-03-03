indicePoluicao = int(input('Digite o índice de poluição: '))
if indicePoluicao >= 0.0 and indicePoluicao <= 2.0:
    print('Ação: Considerar Aceitável')
elif indicePoluicao > 2.0 and indicePoluicao <= 5.0:
    print('Ação: Suspender Atividades Grupo I')
if indicePoluicao > 6.0 and indicePoluicao <= 7.0:
    print('Ação: Suspender Atividades Grupo I e II')
elif indicePoluicao > 8.0:
    print('Ação: Suspender Atividades de todos os grupos e fechar as indústrias')
