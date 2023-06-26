

times = ('Palmeiras',
'Corinthians',
'Fluminense',
'Atlético-MG',
'Athletico-PR',
'Flamengo',
'Internacional',
'Bragantino',
'Santos',
'São Paulo',
'Botafogo',
'Ceará',
'Coritiba',
'Goiás',
'América-MG',
'Avaí',
'Cuiabá',
'Atlético-GO',
'Juventude',
'Fortaleza')

print(f'Os 5 primeiros times na tabela do campeonato brasileiro são: {times[:5]}\n'
      f'Os 4 últimos times na tabela do campeonato brasileiro são: {times[-4:]}\n'
      f'Em ordem alfabetica se classificam: {sorted(times)}\n'
      f'O time do Atletico-MG está posicionado em {times.index("Atlético-MG") +1}ª lugar '
      )
