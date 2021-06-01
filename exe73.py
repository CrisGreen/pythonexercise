'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

print('=-' * 30)
times = 'corintias', 'vasco', 'flamengo', 'santos', 'csa', 'crb'
print(f'Lista de times do brasileirao {times}')
print('=-' * 30)
print(f'Os 5 primeiros times sao {times[0:5]}')
print('=-' * 30)
print(f'Os 4 ultimos sao {times[-4:]}')
print('=-' * 30)
print(f'Times em ordem alfabetica {sorted(times)}')
print('=-' * 30)
print(f' O flamengo esta na {times.index("flamengo")+1} posicao')
