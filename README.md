## Sobre o Projeto
O Mission Control AI é um sistema desenvolvido em Python com o objetivo de realizar o monitoramento inteligente e automatizado de uma missão espacial experimental. O software organiza dados operacionais em uma estrutura matricial, analisa dinamicamente cada ciclo de telemetria, gera alertas, calcula o nível de risco de cada etapa, determina a tendência geral da operação e indica de forma automatizada qual área do sistema foi mais severamente impactada ao longo do tempo.

---

## Detalhes da Missão e Identificação
* **Nome da Missão:** Orion Gamma
* **Nome da Equipe:** Omega
* **Turma:** 1CCA

### Integrantes da Equipe
* Thiago Soalheiro Diamantino - RM: 569316
* Kauan Damasceno de Lima - RM: 573727

---

### 1. Estrutura de Dados (Matriz de Telemetria)
Os dados brutos da missão são armazenados em uma matriz bidimensional chamada `dados_missao`. Cada linha representa um Ciclo de Monitoramento (um momento específico no tempo) e as colunas contêm os valores numéricos dos indicadores na seguinte ordem posicional fixa:
* Índice 0: Temperatura interna (°C)
* Índice 1: Comunicação com a base (%)
* Índice 2: Sistema de energia / Bateria (%)
* Índice 3: Suporte de oxigênio (%)
* Índice 4: Estabilidade operacional (%)

### 2. Funções de Análise e Regras
O sistema possui funções de análise individuais para cada uma das cinco variáveis monitoradas. Cada função avalia o parâmetro recebido e retorna uma tupla contendo o status textual (NORMAL, ATENÇÃO ou CRÍTICO) e a pontuação de risco correspondente (0, 1 ou 2 pontos):

* **Temperatura interna (`analisar_temperatura`):**
  * NORMAL (0 pts): Entre 18°C e 30°C.
  * ATENÇÃO (1 pt): Menor que 18°C OU entre 31°C e 35°C.
  * CRÍTICO (2 pts): Maior que 35°C.

* **Comunicação com a base (`analisar_comunicacao`):**
  * NORMAL (0 pts): 60% ou mais.
  * ATENÇÃO (1 pt): Entre 30% e 59%.
  * CRÍTICO (2 pts): Menor que 30%.

* **Sistema de energia / Bateria (`analisar_bateria`):**
  * NORMAL (0 pts): 50% ou mais.
  * ATENÇÃO (1 pt): Entre 20% e 49%.
  * CRÍTICO (2 pts): Menor que 20%.

* **Suporte de oxigênio (`analisar_oxigenio`):**
  * NORMAL (0 pts): 90% ou mais.
  * ATENÇÃO (1 pt): Entre 80% e 89%.
  * CRÍTICO (2 pts): Menor que 80%.

* **Estabilidade operacional (`analisar_estabilidade`):**
  * NORMAL (0 pts): 70% ou mais.
  * ATENÇÃO (1 pt): Entre 40% e 69%.
  * CRÍTICO (2 pts): Menor que 40%.

### 3. Processamento dos Ciclos e Cálculo de Risco
O algoritmo percorre a matriz linha por linha por meio de uma estrutura de repetição `while`. Dentro do loop:
* Os dados de cada coluna são desestruturados.
* As respectivas funções de análise são invocadas para avaliar cada indicador.
* A pontuação de risco de cada indicador é somada, gerando o risco total do ciclo (escala de 0 a 10 pontos).
* O ciclo é classificado globalmente pela função `classificar_ciclo` seguindo a seguinte distribuição:
  * 0 a 2 pontos: MISSÃO ESTÁVEL
  * 3 a 5 pontos: MISSÃO EM ATENÇÃO
  * 6 a 10 pontos: MISSÃO CRÍTICA

### 4. Estatísticas Acumuladas e Relatório Final
Ao mesmo tempo em que os ciclos são processados, variáveis acumuladoras coletam dados para consolidar a análise analítica global:
* **Médias Aritméticas:** Valores de cada indicador são somados individualmente e, ao final, divididos pelo total de ciclos para obter a média da missão.
* **Ciclo Mais Crítico:** Uma estrutura condicional verifica se o risco do ciclo atual é maior do que o maior risco registrado anteriormente. Caso seja, o sistema armazena o índice do ciclo e a pontuação para reportá-los como o ponto mais crítico.
* **Mapeamento da Área Mais Afetada:** Uma lista unidimensional chamada `riscos_area` de tamanho 5 funciona como contadora. Toda vez que um indicador pontua risco (1 ou 2), essa pontuação é adicionada ao índice correspondente da área. Ao final, um loop manual varre essa lista para identificar qual índice obteve o maior valor acumulado, determinando o sistema mais severamente afetado.
* **Análise de Tendência Operacional:** A função `analisar_tendencia` avalia o primeiro e o último elemento da lista de riscos armazenados. Se a pontuação do último ciclo for menor que a do primeiro, a tendência é de melhoria. Se for maior, a tendência é de piora. Se forem iguais, a situação permaneceu estável.

---

## Como Executar o Código

### Pré-requisitos
* Ter o Python instalado no computador (versão 3.10 ou superior recomendada).
* Um terminal (Prompt de Comando, PowerShell ou Terminal do Linux/macOS) ou um ambiente de desenvolvimento como o VS Code.

### Passo a Passo para Execução
1. Faça o download ou clone o repositório em sua máquina:
```bash
   git clone https://github.com/o-kauan/1CCA---Global_Solution---1semestre.git

```

2. Acesse o diretório do projeto via terminal:
```bash
cd mission-control-ai

```


3. Execute o script principal utilizando o interpretador do Python:
```bash
python mission_control.py

```


4. Os resultados das análises individuais de cada ciclo e o relatório final detalhado serão exibidos diretamente no terminal.

---
