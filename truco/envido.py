
class Envido():
    
    def __init__(self):
        self.jogador1_pontos = 0
        self.jogador2_pontos = 0
        self.tipo_envido = ""
        self.valor_envido = 2
        self.valor_final = 0
        self.ultimo_tipo_envido = ""
        self.jogador_pediu_envido = 0
        self.jogador_pediu_real_envido = 0
        self.jogador_pediu_falta_envido = 0

        
    def jogador_pediu_envido(self, quem_pediu, jogador1, jogador2, jogador1_pontos, jogador2_pontos):
        self.jogador1_pontos = 0
        self.jogador2_pontos = 0
        self.tipo_envido = "Envido"
        self.ultimo_tipo_envido = "Envido"
        print("Jogador pediu Envido")

        if(quem_pediu == 1):
            escolha = jogador2.avaliarEnvido()
            self.jogador_pediu_envido = 1

        else:
            self.jogador_pediu_envido = 2
            escolha -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            print(f"fugiu")
            if(quemPediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False
        
    def jogador2_aceitou_envido(self):
        if self.tipo_envido == "Envido":
            self.tipo_envido = "Envido"
            print("Jogador 2 aceitous Envido")
            ganhador = self.determine_ganhador()
            if ganhador == 1:
                self.jogador1_pontos += self.valor_envido
            elif ganhador == 2:
                self.jogador2_pontos += self.valor_envido
            print("Jogador 1 pontos:", self.jogador1_pontos)
            print("Jogador 2 pontos:", self.jogador2_pontos)
        else:
            print("Jogada inválida")
    
    def jogador2_fugiu_envido(self):
        if self.tipo_envido == "Envido":
            self.tipo_envido = "Envido"
            print("Jogador 2 fugius Envido")
            self.jogador2_pontos -= 1
            print("Jogador 2 pontos:", self.jogador2_pontos)
        else:
            print("Jogada inválida")
        
    def jogador2_pediu_real_envido(self):
        if self.tipo_envido == "Envido" or self.tipo_envido == "Real Envido":
            self.tipo_envido = "Real Envido"
            self.valor_envido = 5
            self.ultimo_tipo_envido = "Real Envido"
            print("Jogador 2 pediu Real Envido")
        else:
            print("Jogada inválida")

    def jogador1_aceitou_real_envido(self):
        if self.tipo_envido == "Real Envido":
            self.tipo_envido = "Real Envido"
            print("Jogador 1 aceitous Real Envido")
            ganhador = self.determine_ganhador()
            if ganhador == 1:
                self.jogador1_pontos += self.valor_envido
            elif ganhador == 2:
                self.jogador2_pontos += self.valor_envido
            print("Jogador 1 pontos:", self.jogador1_pontos)
            print("Jogador 2 pontos:", self.jogador2_pontos)
        else:
            print("Jogada inválida")

    def jogador1_fugiu_real_envido(self):
        if self.tipo_envido == "Real Envido":
            self.tipo_envido = "Real Envido"
            print("Jogador 1 fugius Real Envido")
            if self.ultimo_tipo_envido == "Envido":
                self.jogador1_pontos -= 1
            elif self.ultimo_tipo_envido == "Real Envido":
                self.jogador1_pontos -= 2
            print("Jogador 1 pontos:", self.jogador1_pontos)
        else:
            print("Jogada inválida")
            
    def jogador1_pediu_falta_envido(self):
        if self.tipo_envido == "Real Envido":
            self.tipo_envido = "Falta Envido"
            self.valor_envido = self.valor_final - max(self.jogador1_pontos, self.jogador2_pontos) # Substituir pela pontuação do jogo nesse momento
            self.ultimo_tipo_envido = "Falta Envido"
            print("Jogador 1 pediu Falta Envido")
        else:
            print("Jogada inválida")

    def jogador2_aceitou_falta_envido(self):
        if self.tipo_envido == "Falta Envido":
            self.tipo_envido = "Falta Envido"
            print("Jogador 2 aceitous Falta Envido")
            ganhador = self.determine_ganhador()
            if ganhador == 1:
                    self.jogador1_pontos += self.valor_envido
            elif ganhador == 2:
                self.jogador2_pontos += self.valor_envido
            print("Jogador 1 pontos:", self.jogador1_pontos)
            print("Jogador 2 pontos:", self.jogador2_pontos)
        else:
            print("Jogada inválida")

    def jogador2_fugiu_falta_envido(self):
        if self.tipo_envido == "Falta Envido":
            self.tipo_envido = "Falta Envido"
            print("Jogador 2 fugius Falta Envido")
            if self.ultimo_tipo_envido == "Real Envido":
                self.jogador2_pontos -= 1
            elif self.ultimo_tipo_envido == "Falta Envido":
                self.jogador2_pontos -= 5
            print("Jogador 2 pontos:", self.jogador2_pontos)
        else:
            print("Jogada inválida")
    
    def avaliar_ganhador(self):
        jogador1_envido_pontos = self.calculate_envido_pontos()
        jogador2_envido_pontos = self.calculate_envido_pontos()
        if jogador1_envido_pontos > jogador2_envido_pontos:
            return 1
        elif jogador2_envido_pontos > jogador1_envido_pontos:
            return 2
        else:
            return 0
        
    def calcular_pontos_envido(self):
        pass

    def loop_resposta_envido(self):
        pass