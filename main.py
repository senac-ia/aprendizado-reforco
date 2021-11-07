import random

modelo = {
  "frio": 
    {
      "devagar": [ 
        (1.0, "frio", +1)
      ],
      "rapido": [
        (0.5, "frio", +2),
        (0.5, "quente", +2)
    ]
  },
  "quente": {
    "devagar": [
      (0.5, "frio", +1),
      (0.5, "quente", +1)
    ],
    "rapido": [
      (1.0, "sobreaquecido", -10),
    ],
  },
  "sobreaquecido": {}
}

timing = 10
estado = "frio"
melhor_acoes = [""]
lista_estados = ["frio"]
recompensa_max = 0
contagem = 0
max_geracoes = 10000

while True:
  acoes = [""]
  estado = "frio"
  estados = [estado]
  recompensa = 0
  contagem += 1

  for i in range(timing):
    acoes_disponiveis = modelo[estado]

    if len(acoes_disponiveis) == 0:
      break
    elif len(acoes_disponiveis) == 1:
      estados_disponiveis = next(iter(acoes_disponiveis.items()))
      acao = estados_disponiveis[0]
    else:
      acao = random.choices(["devagar", "rapido"])[0]
      estados_disponiveis = acoes_disponiveis[acao]

    estado_prox = random.choices(estados_disponiveis)[0]

    estado = estado_prox[1] # pega próximo estado
    recompensa += estado_prox[2] # atualiza recompensa

    #print(str(i) + "\t" + acao + "\t" + estado)

    if estado == "sobreaquecido":
      break

    acoes.append(acao)
    estados.append(estado)
  
  if recompensa >= recompensa_max:
    recompensa_max = recompensa
    melhor_acoes = acoes
    lista_estados = estados

  if contagem >= max_geracoes:
    break

print("Recompensa:\t" + str(recompensa_max))
print("Ações:\t\t" + str(melhor_acoes))
print("Estados:\t" + str(lista_estados))