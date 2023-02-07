class Envido():
    def __init__(self):
        self.valor_envido = 2
        self.ultimo_tipo_envido = ""
        self.jogador_pediu_envido = 0
        self.jogador_pediu_real_envido = 0
        self.jogador_pediu_falta_envido = 0
        self.quem_fugiu = 0

        
    def pedir_envido(self, quem_pediu, jogador1, jogador2):
        self.ultimo_tipo_envido = "Envido"
        print("Jogador pediu Envido")

        if (quem_pediu == 1):
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliar_envido()

        else:
            self.jogador_pediu_envido = 2
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1.nome}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if (quem_pediu == jogador1):
                jogador1.pontos += 1
                return

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print('aceitou envido')
            self.avaliar_vencedor_envido(quem_pediu, jogador1, jogador2)

        elif escolha == 2:
            print(f'Real Envido')
            self.jogador_pediu_real_envido(quem_pediu, jogador1, jogador2)
        
        else:
            print(f'Falta Envido')
            self.jogador_pediu_falta_envido(quem_pediu, jogador1, jogador2)

        
    def jogador_pediu_real_envido(self, quem_pediu, jogador1, jogador2):
        self.ultimo_tipo_envido = "Real Envido"
        print("Jogador pediu Envido")

        if (quem_pediu == 1):
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliar_envido()

        else:
            self.jogador_pediu_envido = 2
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1.nome}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if (quem_pediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False
        
        elif escolha == 1:
            print('aceitou Real envido')
            self.avaliar_vencedor_envido(quem_pediu, jogador1, jogador2)
        
        else:
            print(f'Falta Envido')
            self.jogador_pediu_falta_envido(quem_pediu, jogador1, jogador2)


    def jogador_pediu_falta_envido(self, quem_pediu, jogador1, jogador2):
        self.ultimo_tipo_envido = "Falta Envido"
        print("Jogador pediu Envido")

        if (quem_pediu == 1):
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliar_envido()

        else:
            self.jogador_pediu_envido = 2
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1.nome}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if (quem_pediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print('aceitou Falta envido')
            self.avaliar_vencedor_envido(quem_pediu, jogador1, jogador2)

    
    def avaliar_vencedor_envido(self, quem_pediu, jogador1, jogador2):
        jogador1_pontos = jogador1.retorna_pontos_envido()
        jogador2_pontos = jogador2.retorna_pontos_envido()

        if jogador1_pontos > jogador2_pontos:
            jogador1.pontos += self.valor_envido

        elif jogador2_pontos > jogador1_pontos:
            jogador1.pontos += self.valor_envido
            
        else:
            quem_pediu.pontos += self.valor_envido


    def retornar_quem_fugiu(self):
        return self.quem_fugiu


    def resetar_pontos_envido(self):
        self.valor_envido = 2
        self.ultimo_tipo_envido = ""
        self.jogador_pediu_envido = 0
        self.jogador_pediu_real_envido = 0
        self.jogador_pediu_falta_envido = 0
        self.quem_fugiu = 0