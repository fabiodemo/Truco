
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
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliarEnvido()

        else:
            self.jogador_pediu_envido = 2
            escolha -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1.nome}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if(quem_pediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print('aceitou envido')

        elif escolha == 2:
            print(f'Real Envido')
            self.jogador_pediu_real_envido(quem_pediu, jogador1, jogador2, jogador1_pontos, jogador2_pontos)
        
        else:
            print(f'Falta Envido')
            self.jogador_pediu_falta_envido(quem_pediu, jogador1, jogador2, jogador1_pontos, jogador2_pontos)

        
        
    def jogador_pediu_real_envido(self, quem_pediu, jogador1, jogador2, jogador1_pontos, jogador2_pontos):
        self.jogador1_pontos = 0
        self.jogador2_pontos = 0
        self.tipo_envido = "Envido"
        self.ultimo_tipo_envido = "Envido"
        print("Jogador pediu Envido")

        if(quem_pediu == 1):
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliarEnvido()

        else:
            self.jogador_pediu_envido = 2
            escolha -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1.nome}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if(quem_pediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False
        
        elif escolha == 1:
            print('aceitou Real envido')
        
        else:
            print(f'Falta Envido')
            self.jogador_pediu_falta_envido(quem_pediu, jogador1, jogador2, jogador1_pontos, jogador2_pontos)


    def jogador_pediu_falta_envido(self, quem_pediu, jogador1, jogador2, jogador1_pontos, jogador2_pontos):
        self.jogador1_pontos = 0
        self.jogador2_pontos = 0
        self.tipo_envido = "Envido"
        self.ultimo_tipo_envido = "Envido"
        print("Jogador pediu Envido")

        if(quem_pediu == 1):
            self.jogador_pediu_envido = 1
            escolha = jogador2.avaliarEnvido()

        else:
            self.jogador_pediu_envido = 2
            escolha -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1.nome}, você aceita o pedido de envido?"))
        

        if escolha == 0:
            print(f"fugiu")
            if(quem_pediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print('aceitou Falta envido')

    
    def avaliar_ganhador(self, jogador1, jogador2):
        jogador1_pontos = jogador1.calculaEnvido()
        jogador2_pontos = jogador2.calculaEnvido()
        if jogador1_pontos > jogador2_pontos:
            return 1
        elif jogador2_pontos > jogador1_pontos:
            return 2
        else:
            return 0

    def loop_resposta_envido(self):
        pass