print(f'Programa de empréstimos.'
      f'Responda: (0-Não ou 1-Sim)')
nome_negativado = int(input('Possui nome negativado? '))
if nome_negativado == 1: #SIM
    print('Não pode realizar empréstimo')
else:
    carteira_assinada = int(input('Possui carteira assinada? '))
    if carteira_assinada == 0: #NÃO
        print('Não pode realizar empréstimo')
    else:
        possui_casa_propria = int(input('Possui casa própria? '))
        if possui_casa_propria == 0: #NÃO
            print('Não pode realizar empréstimo')
        else:
            print('Conceder empréstimo')