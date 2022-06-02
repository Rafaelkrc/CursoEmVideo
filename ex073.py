times = 'Corinthians', 'Santos', 'América', 'Red Bull Bragantino', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Internacional', 'Coritiba', 'Avaí', 'Cuiabá', 'Athletico Paranaense', 'Palmeiras', 'Flamengo',  'Fluminense', 'Goiás', 'Ceará', 'Juventude', 'Atlético GO', 'Fortaleza'
print('=' * 80)
print(f'Lista de times do Brasileira: {times}')
print('=' * 80)
print('Os 5 primeiros times sao:', times[0:5])
print('=' * 80)
print('Os ultimos 4 times sao', times[16:])
print('=' * 80)
print(sorted(times))
print('=' * 80)
print(f'O time do Botafogo esta na {times.index("Botafogo") + 1}° posicao')
print('=' * 80)

