# Population Algorithm - Problema da Mochila Binária

## Sobre projeto

Experimento com o algoritmo populacional evolucionário para resolver o problema da mochila binária,
no qual dado uma mochila, quais objetos posso carregar a fim de maximizar o meu lucro?

Utilizando duas instâncias diferentes do conjunto de Benchmarks disponível em neste [link de datasets](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)

Para cada instância foi realizado:

- 30 Execuções
- Calculo da média
- Desvio padrão

Com estas informações, identificando a melhor solução e gerando um artigo

## Como executar o projeto

Primeiro você deve instalar em sua máquina o poetry. Este é um gerenciador de dependências de projetos Python.

Utilizando  osx / linux / bashonwindows:
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```

ou utilizando Windows Powershell:
```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

Após instalar ele clone este repositório, e estando na raiz do projeto rode o seguinte comando:

```sh
poetry shell
```

Este comando ira criar a `virtual env` do projeto e inicializar ela.