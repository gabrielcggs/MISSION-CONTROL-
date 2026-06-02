"""Mission Control AI - Global Solution 2026.1

Projeto didatico para monitoramento de ciclos de uma missao espacial.
"""

NOME_MISSAO = "Carina Teste"
NOME_EQUIPE = "Equipe 3G"

# Ordem obrigatoria em cada ciclo:
# [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional",
]


def analisar_temperatura(valor):
    if valor < 18:
        return "ATENCAO", 1, "Temperatura abaixo do ideal"
    if valor <= 30:
        return "NORMAL", 0, "Temperatura estavel"
    if valor <= 35:
        return "ATENCAO", 1, "Temperatura elevada"
    return "CRITICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRITICO", 2, "Comunicacao em nivel critico"
    if valor <= 59:
        return "ATENCAO", 1, "Comunicacao instavel"
    return "NORMAL", 0, "Comunicacao estavel"


def analisar_bateria(valor):
    if valor < 20:
        return "CRITICO", 2, "Bateria em nivel critico"
    if valor <= 49:
        return "ATENCAO", 1, "Bateria abaixo do recomendado"
    return "NORMAL", 0, "Energia estavel"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRITICO", 2, "Oxigenio em nivel critico"
    if valor <= 89:
        return "ATENCAO", 1, "Oxigenio abaixo do ideal"
    return "NORMAL", 0, "Oxigenio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRITICO", 2, "Estabilidade operacional critica"
    if valor <= 69:
        return "ATENCAO", 1, "Estabilidade operacional reduzida"
    return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontos):
    if pontos <= 2:
        return "MISSAO ESTAVEL"
    if pontos <= 5:
        return "MISSAO EM ATENCAO"
    return "MISSAO CRITICA"


def analisar_tendencia(riscos):
    primeiro = riscos[0]
    ultimo = riscos[-1]
    if ultimo > primeiro:
        return "A missao apresentou tendencia de piora."
    if ultimo < primeiro:
        return "A missao apresentou tendencia de melhora."
    return "A missao permaneceu estavel em relacao ao inicio."


def identificar_area_mais_afetada(pontos_por_area):
    maior_pontuacao = max(pontos_por_area)
    indice = pontos_por_area.index(maior_pontuacao)
    return areas_monitoradas[indice], maior_pontuacao


def gerar_recomendacao(statuses):
    if all(status == "NORMAL" for status in statuses):
        return "Manter operacao normal e continuar monitoramento."

    recomendacoes = []
    if statuses[0] == "CRITICO":
        recomendacoes.append("verificar controle termico")
    if statuses[1] == "CRITICO":
        recomendacoes.append("restabelecer comunicacao com a base")
    if statuses[2] == "CRITICO":
        recomendacoes.append("ativar modo de economia de energia")
    if statuses[3] == "CRITICO":
        recomendacoes.append("acionar protocolo de suporte a vida")
    if statuses[4] == "CRITICO":
        recomendacoes.append("reduzir operacoes nao essenciais")

    if recomendacoes:
        return "Acao imediata: " + "; ".join(recomendacoes) + "."

    return "Monitorar sistemas em atencao e preparar plano de contingencia."


def calcular_medias(matriz):
    quantidade = len(matriz)
    soma_colunas = [0, 0, 0, 0, 0]

    for ciclo in matriz:
        for i, valor in enumerate(ciclo):
            soma_colunas[i] += valor

    return [soma / quantidade for soma in soma_colunas]


def exibir_cabecalho():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missao: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)


def gerar_relatorio_final(riscos, pontos_por_area):
    medias = calcular_medias(dados_missao)
    ciclo_mais_critico_indice = riscos.index(max(riscos))
    risco_medio = sum(riscos) / len(riscos)
    ciclos_criticos = sum(1 for r in riscos if r >= 6)
    area_mais_afetada, pontos_area = identificar_area_mais_afetada(pontos_por_area)
    classificacao_final = classificar_ciclo(round(risco_medio))
    tendencia = analisar_tendencia(riscos)

    print("=" * 60)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 60)
    print(f"Missao: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print(f"Media de temperatura: {medias[0]:.2f} C")
    print(f"Media de comunicacao: {medias[1]:.2f}%")
    print(f"Media de bateria: {medias[2]:.2f}%")
    print(f"Media de oxigenio: {medias[3]:.2f}%")
    print(f"Media de estabilidade: {medias[4]:.2f}%")
    print(f"Ciclo mais critico: Ciclo {ciclo_mais_critico_indice + 1}")
    print(f"Maior pontuacao de risco: {max(riscos)}")
    print(f"Risco medio da missao: {risco_medio:.2f}")
    print(f"Quantidade de ciclos criticos: {ciclos_criticos}")
    print("Tendencia da missao:")
    print(tendencia)
    print("Pontuacao acumulada por area:")
    for i, area in enumerate(areas_monitoradas):
        print(f"{area}: {pontos_por_area[i]} pontos")
    print("Area mais afetada:")
    print(f"{area_mais_afetada} ({pontos_area} pontos)")
    print("Classificacao final da missao:")
    print(classificacao_final)


def executar_monitoramento():
    exibir_cabecalho()

    riscos = []
    pontos_por_area = [0, 0, 0, 0, 0]

    for numero_ciclo, ciclo in enumerate(dados_missao, start=1):
        print(f"CICLO {numero_ciclo}")
        print("-" * 60)

        temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

        analises = [
            analisar_temperatura(temperatura),
            analisar_comunicacao(comunicacao),
            analisar_bateria(bateria),
            analisar_oxigenio(oxigenio),
            analisar_estabilidade(estabilidade),
        ]

        valores = [temperatura, comunicacao, bateria, oxigenio, estabilidade]
        nomes = ["Temperatura", "Comunicacao", "Bateria", "Oxigenio", "Estabilidade"]
        unidades = ["C", "%", "%", "%", "%"]

        pontos_ciclo = 0
        statuses = []

        for i in range(5):
            status, pontos, descricao = analises[i]
            pontos_ciclo += pontos
            pontos_por_area[i] += pontos
            statuses.append(status)
            print(f"{nomes[i]}: {valores[i]} {unidades[i]} | {status} | {descricao}")

        classificacao = classificar_ciclo(pontos_ciclo)
        recomendacao = gerar_recomendacao(statuses)
        riscos.append(pontos_ciclo)

        print(f"Pontuacao de risco do ciclo: {pontos_ciclo}")
        print(f"Classificacao do ciclo: {classificacao}")
        print(f"Recomendacao: {recomendacao}")
        print()

    gerar_relatorio_final(riscos, pontos_por_area)


if __name__ == "__main__":
    executar_monitoramento()
