# Personagem: CLASSE MAE
# HEROI: CONTROLADO PELO O USER
# INIMIGO: OPP


class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def getNome(self):
        return self.__nome
    def getVida(self):
        return self.__vida
    def getNivel(self):
        return self.__nivel

    def mostrarInfo(self):
        return f"NÍVEL: {self.__nivel}\nNOME: {self.__nome}\nVIDA: {self.__vida}"

    # ATAQUES
    def causarDano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def ataque(self, alvo):
        dano = self.__nivel * 3
        alvo.causarDano(dano)
        print(f"{self.getNome()} ATACOU {alvo.getNome()} E CASOU {dano} DE DANOS")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def getHabilidade(self):
        return self.__habilidade

    def ataqueEspecial(self, alvo):
        dano = self.getNivel() * 6
        alvo.causarDano(dano)
        print(f"{self.getNome()} USOU O HABILIDADE ESPECIAL {self.getHabilidade()} EM {alvo.getNome()} E CAUSOU {dano} DE DANOS\n")

    def mostrarInfo(self):
        return f"{super().mostrarInfo()}\nHABILIDADE: {self.getHabilidade()}"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def mostrarInfo(self):
        return f"{super().mostrarInfo()}\nTipo: {self.getTipo()}\n"


class Jogo:
    """ CLASSE ORQUESTRADO """
    def __init__(self):
        nome_heroi = input("NOME DO HEROI: ")
        self.heroi = Heroi(nome = nome_heroi , vida = 100, nivel = 6, habilidade = "LANÇA CHAMAS")
        self.inimigo = Inimigo(nome = "Vilgax", vida = 90, nivel = 5, tipo = "Voador")

    def iniciarBatalha(self):
        """ FAZER A GESTÃO DA BATALHAS"""
        print("A INICIAR A BATALHA!")

        # A VALIAR A VIDA DE CADA PERSONAGEM
        while self.heroi.getVida() > 0 and self.inimigo.getVida() > 0:
            print("INFORMAÇÕES DOS PERSONAGENS")
            print("INFORMAÇÕES DO HEROI")
            print(self.heroi.mostrarInfo())
            print("\n")
            print("INFORMAÇÕES DO INIMIGO")
            print(self.inimigo.mostrarInfo())

            input(f"\nPRESSIONE ENTER PARA ATACAR O {self.inimigo.getNome()}......")
            print("O TIPO DE ATAQUE: \n1 - ATAQUE NORMAL\n2 - ATAQUE ESPECIAL😈😈😈👌🏽")
            escolha = input("ESCOLHA: ")

            if escolha == "1":
                self.heroi.ataque(self.inimigo)
            elif escolha == "2":
                self.heroi.ataqueEspecial(self.inimigo)
            else:
                print("[ERROR] | ESCOLHA INVÁLIDA\n")
            if self.inimigo.getVida() > 0:
                # O INIMIGO A ATACAR O HEROI
                self.inimigo.ataque(self.heroi)
        if self.heroi.getVida() > 0:
            print(f"PARABÉNS {self.heroi.getNome()}, VOCÊ VENCEU A BATALHA\n")
        else:
            print("VOCÊ FOI DERROTADA\n")


# A INSTANCIAR A CLASSE JOGO E  A INICIAR A BATALHA
jogo = Jogo()
jogo.iniciarBatalha()

















print("\n")
