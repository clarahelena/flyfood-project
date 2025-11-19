from main_flyfood import leitura_matriz
from lerBrasil58 import custoCaminho

def calc_distancia_manhatan(coordenada1, coordenada2):
    #Coord[0] é o X e Coord[1] é o Y, dos pontos
    #e calcula distância Manhattan: |x1-x2| + |y1-y2|
    return abs(coordenada1[0] - coordenada2[0]) + abs(coordenada1[1] - coordenada2[1])


def criador_matriz(coordenadas):
    #ordena pontos em ordem alfabetica
    pontos = ['R'] + sorted([k for k in coordenadas.keys() if k != 'R'])

    total_pontos = len(pontos)

    matriz = [[0] * total_pontos for _ in range(total_pontos)]

    for i in range(total_pontos):
        for j in range(total_pontos):
            if i != j:
                cidade_I = pontos[i]
                cidade_J = pontos[j]

                coord_i = coordenadas[cidade_I]
                coord_j = coordenadas[cidade_J]

                distancia = calc_distancia_manhatan(coord_i, coord_j)
                matriz[i][j] = distancia

    return pontos, matriz


def conversor_upper_row(matriz):
    #converte uma matriz para o formato triangular superior
    dimensao_matriz = len(matriz)
    linhas = []

    for k in range(dimensao_matriz - 1):
        linha_valores = []

        for j in range (k + 1, dimensao_matriz): #pega só os valores acima da diagonal
            linha_valores.append(str(matriz[k][j]))

        linhas.append(' '.join(linha_valores))

    return linhas


def gerar_tsplib(entradaTXT, saidaTSP): # converter matriz.txt em flyfood.tsp
    #gera um arquivo .tsp no formato TSPLIB
    coordenadas = leitura_matriz(entradaTXT)

    pontos, matriz_distancia = criador_matriz(coordenadas)

    linhas_upper = conversor_upper_row(matriz_distancia)

    with open(saidaTSP, 'w') as f:
        f.write("NAME: flyfood\n")
        f.write("TYPE: TSP\n")
        f.write("COMMENT: Problema de entrega FlyFood\n")
        f.write(f"DIMENSION: {len(pontos)}\n")
        f.write("EDGE_WEIGHT_TYPE: EXPLICIT\n") #Como ja fizemos o calculo da distancia manhtan, o type é explicit
        f.write("EDGE_WEIGHT_FORMAT: UPPER_ROW\n")
        f.write("EDGE_WEIGHT_SECTION\n")

        for linha in linhas_upper:
            f.write(linha + '\n')
    
    return pontos, matriz_distancia


def ler_tsplib_upper_row(caminho_tsp):
    with open(caminho_tsp, "r") as f: #abre o arquivo e o atribui a variável "f"
        linhas = f.readlines() #lê todo conteúdo do arquivo, retorna uma lista de strings e a armazena na variável "linhas"

    N = None #variável em que vão ficar armazenadas as dimenções da matriz
    lendo_matriz = False #indica se o loop entrou no trecho onde tem o "EDGE_WEIGHT_SECTION"
    upper_rows = [] # armazena as linhas de números do triângulo superior

    for linha in linhas: #loop para percorrer cada linha do arquivo
        linha = linha.strip() #limpa a linha

        if linha.upper().startswith("DIMENSION"): #transforma o coteúdo da linha em maiúsculo e verifica se começa com "DIMENSION"
            partes = linha.split(":")
            if len(partes) >= 2:
                N = int(partes[1].strip())

        if linha.upper().startswith("EDGE_WEIGHT_SECTION"):
            lendo_matriz = True
            continue

        if lendo_matriz:
            if linha.upper() == "EOF":
                break
            if linha != "":
                numeros = linha.split()
                upper_rows.append([int(x) for x in numeros])

    matriz = [[0 for _ in range(N)] for _ in range(N)]

    for k in range(N - 1):
        linha_upper = upper_rows[k]
        for j, valor in enumerate(linha_upper):
            matriz[k][k + 1 + j] = valor

    for i in range(N):
        for j in range(i + 1, N):
            matriz[j][i] = matriz[i][j]

    return matriz


def matriz_para_dicionario(matriz_lista):
    dicionario = {}
    for indiceLinha, linha in enumerate(matriz_lista): #indices das linhas e colunas
        for indiceColuna, valor in enumerate(linha):
                if indiceLinha != indiceColuna:
                    dicionario[(indiceLinha+1, indiceColuna+1)] = valor #dicionario com os indices das linhas e colunas, e o valor 
    return dicionario



if __name__ == "__main__":
    entrada_txt = "matriz.txt"
    saida_tsp = "flyfood.tsp"

    gerar_tsplib("matriz.txt", "flyfood.tsp")
    matriz = ler_tsplib_upper_row("flyfood.tsp") # ler arquivo TSPLIB e reconstruir matriz
    
    dicionario = matriz_para_dicionario(matriz) # transforma a matriz em dicionario pra ser usada na função custoCaminho
    
    rota = [1, 2, 5, 4, 3] # usando a melhor rota do flyfood como teste (R → A → D → C → B)
    '''
    Como a matriz foi criada ordenada alfabeticamente, então A = 2, B = 3 ....começa em 2 pois o R ja é o 1
    '''
    custo = custoCaminho(rota, dicionario)
    
    # 5. Exibir resultado
    print(f"Custo da rota {rota}: {custo}")