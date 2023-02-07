class Envido():
    def __init__(self):
        self.valor_envido = 2
        self.estado_atual = ""
        self.jogador_pediu_envido = 0
        self.real_envido = 0
        self.falta_envido = 0
        self.quem_fugiu = 0
        self.jogador_bloqueado = 0

    def reverter_jogador_bloqueado(self):
        """Lógica para impedir que o mesmo jogador não peça o aumento de aposta seguidamente."""
        if (self.jogador_bloqueado == 1):
            self.jogador_bloqueado = 2
        
        else:
            self.jogador_bloqueado = 1


    def inicializar_jogador_bloqueado(self, quem_pediu):
        """Inicialização do jogador que foi bloqueado e não pode pedir aumento da aposta do jogo."""
        self.jogador_bloqueado = quem_pediu

    def controlar_envido(self, tipo, quem_pediu, jogador1, jogador2):
        if (self.estado_atual != "" or tipo == self.estado_atual):
            return None
        
        if (quem_pediu == self.jogador_bloqueado):
            return None
        else:
            self.inicializar_jogador_bloqueado(quem_pediu)

        if (tipo == 'Envido'):
            self.envido(quem_pediu, jogador1, jogador2)

        elif (tipo == 'Real Envido'):
            self.real_envido(quem_pediu, jogador1, jogador2)

        elif (tipo == 'Falta Envido'):
            self.falta_envido(quem_pediu, jogador1, jogador2)

        
        
    def envido(self, quem_pediu, jogador1, jogador2):
        self.estado_atual = "Envido"
        self.inicializar_jogador_bloqueado(quem_pediu)
        print("Jogador pediu Envido")

        if (quem_pediu == 1):
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliar_envido()

        else:
            self.jogador_pediu_envido = 2
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"Jogador {quem_pediu}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if (quem_pediu == 1):
                jogador1.pontos += 1
                return

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print('Jogador aceitou envido!')
            self.avaliar_vencedor_envido(quem_pediu, jogador1, jogador2)

        elif escolha == 2:
            print(f'Real Envido')
            self.reverter_jogador_bloqueado()
            self.real_envido(quem_pediu, jogador1, jogador2)
        
        else:
            print(f'Falta Envido')
            self.reverter_jogador_bloqueado()
            self.falta_envido(quem_pediu, jogador1, jogador2)

        
    def real_envido(self, quem_pediu, jogador1, jogador2):
        self.estado_atual = "Real Envido"
        print("Jogador pediu Envido")

        if (quem_pediu == 1):
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliar_envido()

        else:
            self.jogador_pediu_envido = 2
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"Jogador {quem_pediu}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if (quem_pediu == 1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False
        
        elif escolha == 1:
            print('aceitou Real envido')
            self.avaliar_vencedor_envido(quem_pediu, jogador1, jogador2)
        
        else:
            print(f'Falta Envido')
            self.falta_envido(quem_pediu, jogador1, jogador2)


    def falta_envido(self, quem_pediu, jogador1, jogador2):
        self.estado_atual = "Falta Envido"
        print("Jogador pediu Envido")

        if (quem_pediu == 1):
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliar_envido()

        else:
            self.jogador_pediu_envido = 2
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"Jogador {quem_pediu}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if (quem_pediu == 1):
                jogador1.pontos += 5

            else:
                jogador2.pontos += 5

            return False

        elif escolha == 1:
            print('aceitou Falta envido')
            self.avaliar_vencedor_envido(quem_pediu, jogador1, jogador2)

    
    def avaliar_vencedor_envido(self, quem_pediu, jogador1, jogador2):
        jogador1_pontos = jogador1.retorna_pontos_envido()
        jogador2_pontos = jogador2.retorna_pontos_envido()

        if jogador1_pontos >= jogador2_pontos:
            print(f'Jogador 1 ganhou {self.valor_envido} pontos')
            jogador1.pontos += self.valor_envido

        else:
            print(f'Jogador 2 ganhou {self.valor_envido} pontos')
            jogador1.pontos += self.valor_envido

    def avaliar_vencedor_falta_envido(self, quem_pediu, jogador1, jogador2):
        jogador1_pontos = jogador1.retorna_pontos_envido()
        jogador2_pontos = jogador2.retorna_pontos_envido()

        if (quem_pediu == 1):
            self.valor_envido = 12 - jogador1.pontos
            
        else:
            self.valor_envido = 12 - jogador2.pontos

        if jogador1_pontos >= jogador2_pontos:
            jogador1.pontos += self.valor_envido
            self.quem_venceu_flor = 1

        elif jogador2_pontos > jogador1_pontos:
            jogador2.pontos += self.valor_envido
            self.quem_venceu_flor = 2



    def retornar_quem_fugiu(self):
        return self.quem_fugiu


    def resetar_pontos_envido(self):
        self.valor_envido = 2
        self.estado_atual = ""
        self.jogador_pediu_envido = 0
        self.real_envido = 0
        self.falta_envido = 0
        self.quem_fugiu = 0
        self.jogador_bloqueado = 0