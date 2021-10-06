===============
Population Algorithm - Problema da Mochila Binária
===============

.. role:: bash(code)
   :language: bash

.. role:: powershell(code)
   :language: powershell
   
   
===============
Sobre projeto
===============

Experimento com o algoritmo populacional evolucionário para resolver o problema da mochila binária,
no qual dado uma mochila, quais objetos posso carregar a fim de maximizar o meu lucro?

Utilizando duas instâncias diferentes do conjunto de Benchmarks disponível em neste `link de datasets <https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html>`_

Para cada instância foi realizado:

- 30 Execuções
- Calculo da média
- Desvio padrão

Com estas informações, identificando a melhor solução e gerando um artigo

===============
Como executar o projeto
===============

Primeiro você deve instalar em sua máquina o poetry. Este é um gerenciador de dependências de projetos Python.

Utilizando  osx / linux / bashonwindows:

:bash:`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -`.

ou utilizando Windows Powershell:

:powershell:`(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python`.

Após instalar ele clone este repositório, e estando na raiz do projeto rode o seguinte comando:

:bash:`poetry shell`.

Este comando ira criar a `virtual env` do projeto e inicializar ela.

Para executar o projeto, estando na pasta raiz você realizar o seguinte comando:

:bash:`python3 src --debug`.

No qual o parametro `--debug` executa apenas uma vez o algoritmo com valores padrões, no qual você não utiliza nenhum dos Benchmarks.

Você tambem pode executar da seguinte maneira:

:bash:`python3 src -dt one 30 --reset-gen`.

O parametro ``-dt {one}`` serve para você selecionar um entre os oitro benchmarks: *one*, *two*, *three*, *four*, *five*, *six*, *seven*, *eight*.

O segundo parametro, que se trata de um numério serve para você informar quantas execuções seja realizar.

O terceiro parametro serve para você resetar as gerações a cada repetição de execução.


