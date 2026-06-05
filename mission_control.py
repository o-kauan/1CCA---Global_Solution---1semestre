dados_missao = [
    [20, 90, 99, 96, 80],
    [24, 52, 90, 95, 76],
    [36, 50, 75, 89, 35],
    [40, 41, 69, 82, 90],
    [35, 22, 52, 71, 42],
    [30, 0, 30, 70, 30]
]
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

def analisar_temperatura(v):
    if v < 18 or 30 < v <= 35: return "ATENCAO", 1
    if v > 35: return "CRITICO", 2
    return "NORMAL", 0

def analisar_comunicacao(v):
    if v < 30: return "CRITICO", 2
    if v < 60: return "ATENCAO", 1
    return "NORMAL", 0

def analisar_bateria(v):
    if v < 20: return "CRITICO", 2
    if v < 50: return "ATENCAO", 1
    return "NORMAL", 0

def analisar_oxigenio(v):
    if v < 80: return "CRITICO", 2
    if v < 90: return "ATENCAO", 1
    return "NORMAL", 0

def analisar_estabilidade(v):
    if v < 40: return "CRITICO", 2
    if v < 70: return "ATENCAO", 1
    return "NORMAL", 0

def classificar_ciclo(risco):
    if risco <= 2: return "MISSAO ESTAVEL"
    if risco <= 5: return "MISSAO EM ATENCAO"
    return "MISSAO CRITICA"

def analisar_tendencia(primeiro, ultimo):
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    if ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    return "A missão permaneceu estável."

def gerar_recomendacao(status):
    recomendacoes = []
    if status["Temperatura"] == "CRITICO":
        recomendacoes.append("Verificar controle térmico.")
    if status["Comunicação"] == "CRITICO":
        recomendacoes.append("Restabelecer contato com a base.")
    if status["Bateria"] == "CRITICO":
        recomendacoes.append("Ativar economia de energia.")
    if status["Oxigênio"] == "CRITICO":
        recomendacoes.append("Acionar protocolo de suporte à vida.")
    if status["Estabilidade"] == "CRITICO":
        recomendacoes.append("Reduzir operações não essenciais.")
    return recomendacoes

riscos_ciclos = []
riscos_area = [0,0,0,0,0]

print("============================================================")
print("MISSION CONTROL AI")
print("============================================================")
print(f"Missão: Orion Gamma")
print(f"Equipe: Omega")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("============================================================")

ciclo_numero = 1
while ciclo_numero <= len(dados_missao):
    ciclo = dados_missao[ciclo_numero - 1]
    t, c, b, o, e = ciclo

    st = {}
    st["Temperatura"], p1 = analisar_temperatura(t)
    st["Comunicação"], p2 = analisar_comunicacao(c)
    st["Bateria"], p3 = analisar_bateria(b)
    st["Oxigênio"], p4 = analisar_oxigenio(o)
    st["Estabilidade"], p5 = analisar_estabilidade(e)

    pontos = [p1, p2, p3, p4, p5]
    risco = p1 + p2 + p3 + p4 + p5
    riscos_ciclos.append(risco)

    j = 0
    while j < len(pontos):
        riscos_area[j] += pontos[j]
        j += 1

    texto_temperatura = "Temperatura adequada"
    if st["Temperatura"] == "ATENCAO":
        texto_temperatura = "Temperatura elevada"
    elif st["Temperatura"] == "CRITICO":
        texto_temperatura = "Risco de superaquecimento"

    texto_comunicacao = "Comunicação estável"
    if st["Comunicação"] == "ATENCAO":
        texto_comunicacao = "Comunicação instável"
    elif st["Comunicação"] == "CRITICO":
        texto_comunicacao = "Comunicação muito fraca"

    texto_bateria = "Energia estável"
    if st["Bateria"] == "ATENCAO":
        texto_bateria = "Bateria abaixo do recomendado"
    elif st["Bateria"] == "CRITICO":
        texto_bateria = "Bateria crítica"

    texto_oxigenio = "Oxigênio adequado"
    if st["Oxigênio"] == "ATENCAO":
        texto_oxigenio = "Oxigênio abaixo do ideal"
    elif st["Oxigênio"] == "CRITICO":
        texto_oxigenio = "Oxigênio insuficiente"

    texto_estabilidade = "Estabilidade operacional adequada"
    if st["Estabilidade"] == "ATENCAO":
        texto_estabilidade = "Estabilidade operacional reduzida"
    elif st["Estabilidade"] == "CRITICO":
        texto_estabilidade = "Risco de perda de controle"

    print(f"\nCICLO {ciclo_numero}")
    print("------------------------------------------------------------")
    print(f"Temperatura: {t} °C | {st['Temperatura']} | {texto_temperatura}")
    print(f"Comunicação: {c}% | {st['Comunicação']} | {texto_comunicacao}")
    print(f"Bateria: {b}% | {st['Bateria']} | {texto_bateria}")
    print(f"Oxigênio: {o}% | {st['Oxigênio']} | {texto_oxigenio}")
    print(f"Estabilidade: {e}% | {st['Estabilidade']} | {texto_estabilidade}")
    print()
    print(f"Pontuação de risco do ciclo: {risco}")
    print(f"Classificação do ciclo: {classificar_ciclo(risco)}")

    rec = gerar_recomendacao(st)
    if rec:
        print(f"Recomendações:")
        for r in rec:
            print(f" {r}")

    ciclo_numero += 1

quantidade_ciclos = len(dados_missao)
soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0
indice = 0
while indice < quantidade_ciclos:
    soma_temp += dados_missao[indice][0]
    soma_com += dados_missao[indice][1]
    soma_bat += dados_missao[indice][2]
    soma_oxi += dados_missao[indice][3]
    soma_est += dados_missao[indice][4]
    indice += 1

media_temp = soma_temp / quantidade_ciclos
media_com = soma_com / quantidade_ciclos
media_bat = soma_bat / quantidade_ciclos
media_oxi = soma_oxi / quantidade_ciclos
media_est = soma_est / quantidade_ciclos

ciclo_mais_critico = 1
maior_pontuacao = riscos_ciclos[0]
quantidade_criticos = 0
indice = 0
while indice < len(riscos_ciclos):
    if riscos_ciclos[indice] > maior_pontuacao:
        maior_pontuacao = riscos_ciclos[indice]
        ciclo_mais_critico = indice + 1
    if riscos_ciclos[indice] > 5:
        quantidade_criticos += 1
    indice += 1

risco_medio = sum(riscos_ciclos) / quantidade_ciclos

area_mais_afetada = areas_monitoradas[0]
maior_pontos_area = riscos_area[0]
j = 1
while j < len(riscos_area):
    if riscos_area[j] > maior_pontos_area:
        maior_pontos_area = riscos_area[j]
        area_mais_afetada = areas_monitoradas[j]
    j += 1

classificacao_final = classificar_ciclo(round(risco_medio))
conclusao = "A missão apresentou estabilidade geral, mas o monitoramento deve continuar ativo." 
if classificacao_final == "MISSAO EM ATENCAO":
    conclusao = "A missão apresentou instabilidade relevante e requer atenção contínua." 
elif classificacao_final == "MISSAO CRITICA":
    conclusao = "A missão está em situação crítica e precisa de ações urgentes para recuperar as condições." 

print("\n============================================================")
print("RELATÓRIO FINAL DA MISSÃO")
print("============================================================")
print(f"Missão: Orion Gamma")
print(f"Equipe: Omega")
print()
print(f"Quantidade de ciclos analisados: {quantidade_ciclos}")
print()
print(f"Média de temperatura: {media_temp:.2f} °C")
print(f"Média de comunicação: {media_com:.2f}%")
print(f"Média de bateria: {media_bat:.2f}%")
print(f"Média de oxigênio: {media_oxi:.2f}%")
print(f"Média de estabilidade: {media_est:.2f}%")
print()
print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_pontuacao}")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {quantidade_criticos}")
print()
print("Tendência da missão:")
print(analisar_tendencia(riscos_ciclos[0], riscos_ciclos[-1]))
print()
print("Pontuação acumulada por área:")
print(f"Temperatura interna: {riscos_area[0]} pontos")
print(f"Comunicação com a base: {riscos_area[1]} pontos")
print(f"Sistema de energia: {riscos_area[2]} pontos")
print(f"Suporte de oxigênio: {riscos_area[3]} pontos")
print(f"Estabilidade operacional: {riscos_area[4]} pontos")
print()
print(f"Área mais afetada: {area_mais_afetada}")
print()
print("Classificação final da missão:")
print(classificacao_final)
print()
print("Conclusão:")
print(conclusao)