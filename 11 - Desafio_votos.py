import pprint
Canditados_eleições = {
    'Primeiro candidato': 'Maria silva',
    'Segundo canditado': 'Marcos neves',
    'Branco Nulo': 'Nulo'
    
}

Maria_silva = 0
Marcos_neves = 0
Nulo = 0



pp = pprint.PrettyPrinter(depth=4)
pp.pprint(Canditados_eleições)

for i in range(1, 6):
    Votos = input(f'Voto da pessoa número {i}:\n')
    if Votos.lower() == 'primeiro':
        Maria_silva += 1
        print('Voto Para Maria realizado com sucesso. Obrigado!')
    elif Votos.lower() == 'segundo':
        Marcos_neves += 1
        print('Voto para Marcos realizado com sucesso. Obrigado!')
    elif Votos.lower() == 'nulo':
        Nulo += 1
        print('Voto nulo realizado com sucesso. Obrigado!')
    else:
        print('Voto invalido, proximo eleitor.')
    continue

print('-'* 65)

if Maria_silva > Marcos_neves:
    print(f'A Maria Silva ganhou as eleições com o total de votos de: {Maria_silva}')
elif Marcos_neves > Maria_silva:
    print(f'O Marcos Neves ganhou as eleições com o total de votos de: {Marcos_neves}')
else:
    print(f'O total de votos nulos foi: {Nulo}')

print(f'Votos totais para a Maria Silva: {Maria_silva}')
print(f'Votos totais para Marcos Neves: {Marcos_neves}')
print(f'Votos totais nulos: {Nulo}')
