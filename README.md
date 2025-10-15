
<div align="center">

# 🦢 FlyFood

### _Otimização de Rotas de Entrega por Drones_

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) ![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge) ![UFRPE](https://img.shields.io/badge/UFRPE-PISI2-orange?style=for-the-badge)

<img src="https://img.icons8.com/fluency/200/drone.png" alt="Drone Icon" width="120"/>

_Transformando a logística urbana através da otimização inteligente de rotas_

[🚀 Começar](#-como-executar) • [📖 Documentação](#-detalhes-t%C3%A9cnicos) • [👥 Equipe](#-autores) • [🔮 Roadmap](#-trabalhos-futuros)

----------

</div>

## 🌟 Sobre o Projeto

**FlyFood** é uma solução inovadora para o desafio da logística urbana moderna. Utilizando algoritmos de otimização inspirados no clássico **Problema do Caixeiro Viajante (TSP)**, o sistema calcula rotas eficientes para drones de entrega em ambientes urbanos representados por matrizes bidimensionais.

### 💡 Por que FlyFood?

```
🚦 Trânsito Intenso  →  ✈️ Drones Autônomos
💰 Altos Custos      →  🔋 Rotas Otimizadas
⏰ Atrasos           →  📍 Entregas Precisas

```

----------

## 🎯 Características Principais

<table> <tr> <td width="50%">

### 🧮 Algoritmo Exato

Utiliza força bruta para garantir a **melhor solução possível** para rotas com até 10-12 pontos de entrega.

</td> <td width="50%">

### 📏 Distância Manhattan

Cálculo de distância adaptado para movimentação em **grade urbana** (horizontal e vertical).

</td> </tr> <tr> <td width="50%">

### 🔄 Permutações Inteligentes

Testa todas as combinações possíveis de rotas para encontrar o **caminho ideal**.

</td> <td width="50%">

### 💾 Performance

Pré-calcula distâncias entre pontos para **otimizar o tempo de execução**.

</td> </tr> </table>

----------

## 🗂️ Estrutura do Projeto

```
📦 flyfood-project/
┣ 📜 main_flyfood.py          # Código principal do algoritmo
┣ 📄 matriz.txt               # Arquivo de entrada (mapa da cidade)
┗ 📖 README.md                # Documentação completa

```

----------

## 🖥️ Como Executar

### 📋 Pré-requisitos

```bash
# Python 3.9 ou superior
python --version
```

### ⚡ Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/clarahelena/flyfood-project.git
cd flyfood-project

# 2. Prepare seu arquivo matriz.txt
# Exemplo:
echo "45
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0" > matriz.txt

# 3. Execute o programa
python main_flyfood.py

```

### 🎬 Demo

<div align="center">

**Entrada (matriz.txt)**

```
45
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0

```

**↓ Processamento ↓**

**Saída**

```
✅ Melhor rota: A D C B
📏 Distância total: 14 dronômetros

```

</div>

----------

## 🔬 Detalhes Técnicos

### 📊 Análise de Complexidade

<table> <thead> <tr> <th>Função</th> <th>Complexidade</th> <th>Descrição</th> </tr> </thead> <tbody> <tr> <td><code>leitura_matriz()</code></td> <td><strong>O(m × n)</strong></td> <td>Leitura e processamento da matriz</td> </tr> <tr> <td><code>calc_distancia_dois_pontos()</code></td> <td><strong>O(n²)</strong></td> <td>Cálculo de todas as distâncias</td> </tr> <tr> <td><code>encontrar_melhor_rota()</code></td> <td><strong>O(n!)</strong></td> <td>Geração e avaliação de permutações</td> </tr> <tr> <td><strong>Complexidade Total</strong></td> <td><strong>O(n!)</strong></td> <td>Dominada pelas permutações</td> </tr> </tbody> </table>



### 🎓 Conceitos Aplicados

<details> <summary><b>📐 Distância de Manhattan</b></summary>

A distância entre dois pontos é calculada como:

```python
distancia = |x₁ - x₂| + |y₁ - y₂|
```

</details> <details> <summary><b>🔄 Problema do Caixeiro Viajante (TSP)</b></summary>

Problema clássico de otimização combinatória:

-   **Entrada:** Conjunto de cidades e distâncias entre elas
-   **Objetivo:** Encontrar a rota mais curta que visita todas as cidades exatamente uma vez
-   **Classificação:** NP-Difícil

FlyFood adapta o TSP para um contexto de entregas urbanas com drones.

</details>

----------

## 📝 Exemplo Detalhado

### 🗺️ Cenário

```
Matriz 4x5 representando uma cidade:

    1   2   3   4   5
  ┌───┬───┬───┬───┬───┐
1 │ 0 │ 0 │ 0 │ 0 │ D │
  ├───┼───┼───┼───┼───┤
2 │ 0 │ A │ 0 │ 0 │ 0 │
  ├───┼───┼───┼───┼───┤
3 │ 0 │ 0 │ 0 │ 0 │ C │
  ├───┼───┼───┼───┼───┤
4 │ R │ 0 │ B │ 0 │ 0 │
  └───┴───┴───┴───┴───┘

Legenda:
🏠 R = Restaurante (origem)
📦 A, B, C, D = Pontos de entrega
⬜ 0 = Espaço vazio

```

### 🛣️ Melhor Rota Encontrada

```
R → A → D → C → B → R

Cálculo das distâncias:
├─ R(1,4) → A(2,2) = |2-1| + |2-4| = 1 + 2 = 3
├─ A(2,2) → D(5,1) = |5-2| + |1-2| = 3 + 1 = 4
├─ D(5,1) → C(5,3) = |5-5| + |3-1| = 0 + 2 = 2
├─ C(5,3) → B(3,4) = |3-5| + |4-3| = 2 + 1 = 3
└─ B(3,4) → R(1,4) = |1-3| + |4-4| = 2 + 0 = 2

Total: 3 + 4 + 2 + 3 + 2 = 14 dronômetros ✅

```

----------

## 🚧 Roadmap

### 🎯 Versão 2.0 (Em Planejamento)

-   [ ] **Heurísticas Avançadas**
    -   [ ] Algoritmo do Vizinho Mais Próximo
-   [ ] **Recursos Adicionais**
    -   [ ] Consideração de restrições de bateria
-   [ ] **Interface**
    -   [ ] Visualização gráfica das rotas
    -   [ ] Dashboard de métricas

----------

## 📚 Fundamentação Teórica

<div align="center">

Tópicos Abordados

**📊 Teoria da Computação**

Complexidade algorítmica, Classes P e NP

**🔢 Matemática Discreta**

Teoria dos grafos, Permutações e Combinações

**🧮 Otimização**

Problema do Caixeiro Viajante, Heurísticas

**📍 Geometria Computacional**

Distância de Manhattan

</div>

----------

## 👥 Autores

<table> <tr> <td align="center"> <a href="https://github.com/clarahelena"> <img src="https://github.com/clarahelena.png" width="100px;" alt="Clara Helena"/><br /> <sub><b>Clara Helena</b></sub> </a><br /> 💻 📖 </td> <td align="center"> <img src="https://via.placeholder.com/100/4A90E2/FFFFFF?text=DN" width="100px;" alt="Danielly"/><br /> <sub><b>Danielly Mendonça</b></sub><br /> 💻 📊 </td> <td align="center"> <img src="https://via.placeholder.com/100/50C878/FFFFFF?text=LG" width="100px;" alt="Lucas"/><br /> <sub><b>Lucas Gabriel</b></sub><br /> 💻 🔬 </td> <td align="center"> <img src="https://via.placeholder.com/100/FF6B6B/FFFFFF?text=LV" width="100px;" alt="Luiz"/><br /> <sub><b>Luiz Vinicius</b></sub><br /> 💻 📝 </td> </tr> </table> <div align="center">

### 🎓 Universidade Federal Rural de Pernambuco (UFRPE)

**Bacharelado em Sistemas de Informação**  
_Projeto Interdisciplinar para Sistemas de Informação 2 (PISI2)_

----------

### 📧 Contato

Tem dúvidas ou sugestões? Abra uma [issue](https://github.com/clarahelena/flyfood-project/issues) ou entre em contato!

----------

### ⭐ Apoie o Projeto

Se este projeto foi útil para você, considere dar uma estrela! ⭐

[![GitHub Stars](https://img.shields.io/github/stars/clarahelena/flyfood-project?style=social)](https://github.com/clarahelena/flyfood-project)

----------

<sub>Feito com ❤️ pela equipe FlyFood | 2025</sub>

</div>
