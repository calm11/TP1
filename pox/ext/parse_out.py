# Obtem o arquivo de saida de um teste e o exibe.


percentages = []
with open('test_out', 'r') as out:
    for line in out:
      if line.startswith('Percentage of NIC rate:'):
        percentages.append(line.split()[-1])

experiment_order = ['| Jellyfish | TCP 1 Flow  |  ECMP  |',
                    '| Jellyfish | TCP 8 Flows |  ECMP  |',
                    '| Jellyfish | TCP 1 Flow  | 8KSHORT|',
                    '| Jellyfish | TCP 8 Flows | 8KSHORT|']

print("\n\n    |Resultados: Tabela 1 |")
for idx, p in enumerate(percentages):
  print("    %s | %s|" % (experiment_order[idx], p))
