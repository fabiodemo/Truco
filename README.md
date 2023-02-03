# Truco Gaudério

A distribuição das cartas é feita de forma automática e aleatória pelo sistema, não havendo a intervenção de nenhum jogador.

 ### Jogo Truco em Python

- **Jogadores**: 2 ou 4
- **Número de cartas**: 40 (retirando-se 8, 9, 10 e curingas)
- **Distribuição**: 3 cartas para cada participante
- **Objetivo**: O jogador ou a dupla que atingir o total de pontos, ganha a partida.

### Convenções
- **O baralho usado é o baralho espanhol**
- **Sequência de menor para maior**: 4, 5, 6, 7, 10, 11, 12, 1, 2, 3 (de todos os naipes)
- **As manilhas são na sequência de menor para maior**: 7 de ouros, 7 de espadas, 1 de paus e 1 de espadas

### Definições
- **Mão** - Fração da partida, vale 1 ponto e poderá ter seu valor aumentado através das disputas de Truco e Envido. É disputada em melhor de 3 rodadas.
- **Rodada** - É a fração da “mão”, em cada rodada os jogadores mostram uma carta.
- **Falta** - É a diferença entre o placar final do jogo e os pontos da pessoa que está ganhando.
- **Empatar** - Quando a maior carta de cada dupla, numa determinada rodada, tem o mesmo valor.
- **Esconder** - Carta Jogar a carta virada para a mesa, passando assim a não valer nada. Também chamado de carta “coberta”, ou “carta encoberta”.
- **Ir ao baralho** - Quando o jogador ou dupla foge da rodada, entregando os pontos de Truco para o jogador ou dupla adversária.

### Pontos obtidos na disputa de Truco Gaudério
- **Truco** - Disputa para aumentar o valor da “mão” para 2
- **Re-truco** - Disputa para aumentar o valor da “mão” para 3
- **Vale 4** - Disputa para aumentar o valor da “mão” para 4

### Pontos obtidos na disputa de Envido
- **Envido** - Disputa paralela que ocorre durante a primeira rodada de uma mão para aumentar seu valor em até 2 pontos.
- **Real Envido** - Similar ao Envido, mas pode aumentar o valor da mão em até 5 pontos.
- **Falta Envido** - Similar ao Envido, mas pode aumentar o valor da mão para a diferença entre o placar final do jogo e os pontos da pessoa que está ganhando.

### Pontos obtidos na disputa de Flor
- **Flor** - Tipo especial de Envido em que o jogador deve ter 3 cartas do mesmo naipe. É possível aumentar o valor da mão em 3 pontos.
- **Contra-flor** - Uma das possíveis respostas ao pedido de Flor. Pode aumentar o valor da mão em 6 pontos. (Em algumas situações o valor pode ser maior)
- **Contra-flor** e o resto - Disputa similar a Contra-flor que pode aumentar o valor da mão para a diferença entre o placar final do jogo e os pontos da pessoa que está ganhando, além dos pontos da Contra-flor. (Em algumas situações o valor pode ser maior)


### A fundação/base dos códigos no presente projeto, está baseada no repositório original criado pelo usuário anthonyzutter, [disponível em neste link] (https://github.com/anthonyzutter/Truco-Jogo)
