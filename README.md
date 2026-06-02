# Mission Control AI

Projeto da Global Solution 2026.1 para a disciplina de Pensamento Computacional e Automacao com Python.

## Integrantes
- Gabriel Camarosani Gouvea Gonçalves da Silva — RM: 569189 — Turma: 1CCPG
- Gabriel Carvalho Nascimento — RM: 571381 — Turma: 1CCPG
- Guilherme Cedro Pardal Teixeira — RM: 571050 — Turma: 1CCPG

## Nome da missao
Carina teste

## Nome da equipe
Equipe 3G

## Objetivo
Simular o monitoramento de uma missao espacial em ciclos, analisando:
- temperatura
- comunicacao
- bateria
- oxigenio
- estabilidade

O sistema gera:
- alertas por area (NORMAL, ATENCAO, CRITICO)
- pontuacao de risco por ciclo
- classificacao de cada ciclo
- tendencia da missao
- area mais afetada
- relatorio final no terminal

## Estrutura do repositorio
- `mission_control.py`: codigo principal da simulacao
- `README.md`: documentacao do projeto

## Regras de classificacao utilizadas

### Temperatura
- menor que 18: ATENCAO
- de 18 ate 30: NORMAL
- maior que 30 ate 35: ATENCAO
- maior que 35: CRITICO

### Comunicacao
- menor que 30: CRITICO
- de 30 ate 59: ATENCAO
- 60 ou mais: NORMAL

### Bateria
- menor que 20: CRITICO
- de 20 ate 49: ATENCAO
- 50 ou mais: NORMAL

### Oxigenio
- menor que 80: CRITICO
- de 80 ate 89: ATENCAO
- 90 ou mais: NORMAL

### Estabilidade
- menor que 40: CRITICO
- de 40 ate 69: ATENCAO
- 70 ou mais: NORMAL

## Pontuacao de risco
- NORMAL = 0 ponto
- ATENCAO = 1 ponto
- CRITICO = 2 pontos

Classificacao do ciclo:
- 0 a 2 pontos: MISSAO ESTAVEL
- 3 a 5 pontos: MISSAO EM ATENCAO
- 6 a 10 pontos: MISSAO CRITICA

## Como executar no PyCharm
1. Abra a pasta do projeto no PyCharm.
2. Abra o arquivo `mission_control.py`.
3. Clique em Run (ou botao direito > Run 'mission_control').
4. Veja o relatorio no terminal do PyCharm.

## Como executar no terminal
```bash
python mission_control.py
```

