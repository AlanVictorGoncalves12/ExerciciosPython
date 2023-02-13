print('-=' * 20)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
#for t in times:
#    print(t)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)

print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')