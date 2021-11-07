import random

modelo = {
  "frio": 
    {
      "devagar": [ (1.0, "frio", +1) ],
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
melhor_acoes = []
lista_estados = []
recompensa_max = 0
contagem = 0
max_geracoes = 10000

while True:
  acoes = []
  estados = []
  recompensa = 0
  contagem += 1

  for i in range(timing):
    acao = random.choices(["devagar", "rapido"])[0]
    estados_disponiveis = modelo[estado][acao]
    estado_prox = random.choices(estados_disponiveis)[0]

    prox_estado = estado_prox[1] # pega próximo estado
    recompensa += estado_prox[2] # atualiza recompensa
    acoes.append(acao)
    estados.append(prox_estado)

    if prox_estado == "sobreaquecido":
      break
  
  if recompensa >= recompensa_max:
    recompensa_max = recompensa
    melhor_acoes = acoes
    lista_estados = estados

  if contagem >= max_geracoes:
    break

print(recompensa)
print(melhor_acoes)
print(lista_estados)