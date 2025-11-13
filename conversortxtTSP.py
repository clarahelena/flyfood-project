from main_flyfood import leitura_matriz

def calc_distancia_manhatan(coordenada1, coordenada2):
    #Coord[0] é o X e Coord[1] é o Y, dos pontos
    #e calcula distância Manhattan: |x1-x2| + |y1-y2|
    return abs(coordenada1[0] - coordenada2[0]) + abs(coordenada1[1] - coordenada2[1])


def criador_matriz(coordenadas):
    #ordena pontos em ordem alfabetica
    pontos = ['R'] + sorted([k for k in coordenadas.keys() if k != 'R'])
    print(f"Ordem alfabetica dos pontos: {pontos}")

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
    #converte matriz para formato triangular superior
    dimensao_matriz = len(matriz)
    linhas = []

    for k in range(dimensao_matriz - 1):
        linha_valores = []

        for j in range (k + 1, dimensao_matriz): #pega só os valores acima da diagonal
            linha_valores.append(str(matriz[k][j]))

        linhas.append(' '.join(linha_valores))

    return linhas


def gerar_tsplib(entradaTXT, saidaTSP):
    #gera arquivo .tsp no formato TSPLIB
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


if __name__ == "__main__":
    pontos, matriz_dist = gerar_tsplib("matriz.txt", "flyfood.tsp")