import os
import pygame
import random
import time

pygame.init()


WIDTH, HEIGHT = 1024, 740
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tabuleiro", "Perguntas")
CORBACKGROUND = (50, 80, 190)
AZUL = (90,156,164)
clock = pygame.time.Clock()
FPS = 30
lobby = []


#----------- Fontes e Texto --------------#
fonte = pygame.font.SysFont("agency FB",25)
fonte_titulo = pygame.font.SysFont("agency FB",35,True)
fonte_info = pygame.font.SysFont("agency FB",26, False,True)
textinho = fonte.render("Texto de teste", True, (100,100,100))

#----------- Assets --------------#
BLOCK = pygame.image.load(os.path.join("assets", "ISO_TILE_1.png"))
BLOCK_0 = pygame.image.load(os.path.join("assets", "ISO_GRASS.png"))
CROWD = pygame.image.load(os.path.join("assets", "crowd.png"))
PLAYER = pygame.image.load(os.path.join("assets", "ping_1.png"))
PLAYER_1 = pygame.image.load(os.path.join("assets", "ping.png"))
PLAYER_2 = pygame.image.load(os.path.join("assets", "ping_2.png"))
BOTAO_CARTA = pygame.image.load(os.path.join("assets", "carta.png"))
MASKGUI = pygame.image.load(os.path.join("assets", "maskgui.png"))
cartabckground = pygame.image.load(os.path.join("assets", "cartabackground.png"))
badending = pygame.image.load(os.path.join("assets", "badending.png"))
fundo_aviso = pygame.image.load(os.path.join("assets", "fundoendgame.png"))


#---------- Botões --------------#
hitbox_carta = BOTAO_CARTA.get_rect(topleft=(0, 0))

#---------- Temporário --------------#
pos_foco_camera = [int(WIDTH / 2 - BLOCK.get_width() / 2), int(HEIGHT / 2 - BLOCK.get_height() / 2)]

#______Centralização de objetos na tela e funcoes basicas_______#
def center_y(object):
    return HEIGHT/2 - object.get_height()/2
def center_x(object):
    return WIDTH /2 - object.get_width()/2

def Click():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
        else:
            return False
def Click_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        return True
    else:
        return False
def Touch(item, ponto):
    if item.collidepoint(ponto):
        return True
    else:
        return False


#---------- Vars para o gerador de mapas --------------#
inc_y = 35  # Distância em y de um tile ao outro
inc_x = 60 # Distância em x de um tile ao outro
x0, y0 = 0,0 # Valores iniciais de referência para os axis x e y
coord_mapa_comp = []  # Lista para guardar todas as coordenadas e montar o MAPA
coord_mapa_path = []  # Guarda todos os caminhos do MAPA
MAPA = [
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 8, 9, 10, 0, 23, 24, 25, 0),
    (0, 7, 0, 11, 0, 22, 0, 26, 0),
    (0, 6, 0, 12, 0, 21, 0, 27, 0),
    (0, 5, 0, 12, 0, 20, 0, 28, 0),
    (0, 4, 0, 13, 0, 19, 0, 29, 0),
    (0, 3, 0, 14, 0, 18, 0, 30, 0),
    (0, 2, 0, 15, 16, 17, 0, 31, 0),
    (0, 1, 0, 0, 0, 0, 0, 32, 0)]

# Ciclo para criar a lista de coordenadas
for row in MAPA:
    for cell in row:
        coord_mapa_comp.append([cell, x0, y0]) # Blocos do MAPA apenas para construção do tabuleiro
        if cell > 0:
            coord_mapa_path.append([cell, x0, y0]) # Caminho das casas entre os blocos

        x0 += inc_x
        y0 += inc_y
    x0 -= inc_x * (len(row) + 1)
    y0 -= inc_y * (len(row) - 1)


indexing = lambda a: a[0]
coord_mapa_path = sorted(coord_mapa_path,key=indexing)


#----------------Perguntas----------------#
fac_1 = pygame.image.load(os.path.join("perguntas", "perg_1.png"))
fac_2 = pygame.image.load(os.path.join("perguntas", "perg_2.png"))
fac_3 = pygame.image.load(os.path.join("perguntas", "perg_3.png"))
fac_4 = pygame.image.load(os.path.join("perguntas", "perg_4.png"))
fac_5 = pygame.image.load(os.path.join("perguntas", "perg_5.png"))
med_1 = pygame.image.load(os.path.join("perguntas", "perg_6.png"))
med_2 = pygame.image.load(os.path.join("perguntas", "perg_7.png"))
med_3 = pygame.image.load(os.path.join("perguntas", "perg_8.png"))
med_4 = pygame.image.load(os.path.join("perguntas", "perg_9.png"))
med_5 = pygame.image.load(os.path.join("perguntas", "perg_10.png"))
med_6 = pygame.image.load(os.path.join("perguntas", "perg_11.png"))
med_7 = pygame.image.load(os.path.join("perguntas", "perg_12.png"))
med_8 = pygame.image.load(os.path.join("perguntas", "perg_13.png"))
med_9 = pygame.image.load(os.path.join("perguntas", "perg_14.png"))
med_10 = pygame.image.load(os.path.join("perguntas", "perg_15.png"))
med_11 = pygame.image.load(os.path.join("perguntas", "perg_16.png"))
med_12 = pygame.image.load(os.path.join("perguntas", "perg_17.png"))

per_resp = {
    fac_2 : (("Verdadeiro",False),("Falso",True), 2),
    fac_3 : (("Verdadeiro",False),("Falso",True), 5),
    fac_4 : (("Verdadeiro",True),("Falso",False), 6),
    fac_5 : (("Verdadeiro",True),("Falso",False), 4),
    med_1 : (("Verdadeiro",True),("Falso",False), 4),
    med_2 : (("Verdadeiro",False),("Falso",True), 3),
    med_3 : (("Verdadeiro",True),("Falso",False), 2),
    med_4 : (("Verdadeiro",True),("Falso",False), 1),
    med_5 : (("Verdadeiro",True),("Falso",False), 2),
    med_6 : (("Verdadeiro",False),("Falso",True), 2),
    med_7 : (("Verdadeiro",True),("Falso",False), 3),
    med_8 : (("Verdadeiro",False),("Falso",True), 2),
    med_9 : (("Verdadeiro",False),("Falso",True), 4),
    med_10 : (("Verdadeiro",False),("Falso",True), 6),
    med_11 : (("Verdadeiro",False),("Falso",True), 5),
    med_12 : (("Verdadeiro",True),("Falso",False), 3)
}

dimensoes_carta = [cartabckground.get_width(), cartabckground.get_height()]

#---------- Classes --------------#
class Carta():
    valor: int
    fundos = cartabckground

    botao_1 = pygame.image.load(os.path.join("perguntas", "op_long_idle.png"))
    botao_1_pressionado = pygame.image.load(os.path.join("perguntas", "op_long_hover.png"))
    botao_1_hitbox = botao_1.get_rect(topleft=(0, 0))
    botao_2 = pygame.image.load(os.path.join("perguntas", "op_long_idle.png"))
    botao_2_pressionado = pygame.image.load(os.path.join("perguntas", "op_long_hover.png"))
    botao_2_hitbox = botao_1.get_rect(topleft=(0, 0))

    perguntas = list(per_resp.keys()) #Lista das chaves do dicionario de perguntas para pesquisa
    carta_n = 0
    def __init__(self):
        self.fundos = Carta.fundos
        self.botao_1 = Carta.botao_1
        self.botao_2 = Carta.botao_2
        self.titulo = None
        self.enunciado = Carta.perguntas[Carta.carta_n] #Enunciado é a chave numero n
        self.resp = per_resp.get(self.enunciado)
        self.carta_n += 1
        Carta.carta_n += 1

    def __repr__(self):
        return f"Carta: {self.carta_n}"


    def choice(self,jogador, resposta):
        run = True

        while run == True:
            clock.tick(FPS)
            TELA.blit(self.fundos, (center_x(self.fundos), center_y(self.fundos)))
            self.opcoes = self.opcoes = [fonte.render("Comprar Mascara", True, (25, 25, 25)),fonte.render(f"Andar {self.resp[2]} casa(s)!", True,(25, 25, 25))]
            parabens = fonte_titulo.render("Parabéns! Você Acertou!", True, (25, 25, 25))

            TELA.blit(self.botao_1, (center_x(self.botao_1), 300))  # Botao 1
            Carta.botao_1_hitbox.topleft = center_x(self.botao_1), 300

            TELA.blit(self.botao_2, (center_x(self.botao_2), 450))  # Botao 2
            Carta.botao_2_hitbox.topleft = center_x(self.botao_2), 450

            TELA.blit(parabens, (center_x(parabens), 150))
            TELA.blit(self.opcoes[0], (center_x(self.opcoes[0]), 330))
            TELA.blit(self.opcoes[1], (center_x(self.opcoes[1]), 490))

            if Carta.botao_1_hitbox.collidepoint(pygame.mouse.get_pos()):
                self.botao_1 = Carta.botao_1_pressionado

                if Click():
                    self.botao_1 = Carta.botao_1_pressionado
                    jogador.mascaras += 1
                    return [True,0]

            elif Carta.botao_2_hitbox.collidepoint(pygame.mouse.get_pos()):
                self.botao_2 = Carta.botao_2_pressionado
                if Click():
                    return resposta

            else:
                self.botao_1 = Carta.botao_1
                self.botao_2 = Carta.botao_2
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

        pass


    def show(self,jogador):
        run = True

        while run == True:
            clock.tick(FPS)
            TELA.blit(self.fundos,(center_x(self.fundos),center_y(self.fundos)))
            self.opcoes = [fonte.render(self.resp[i][0], True, (25, 25, 25)) for i in range(len(self.resp)-1)]
            self.valor_da_carta = fonte.render(f"Vale {self.resp[2]} casa(s)!", True,(25, 25, 25))
            TELA.blit(self.enunciado,(center_x(self.enunciado),60))


            TELA.blit(self.botao_1, (center_x(self.botao_1), 400)) # Botao 1
            Carta.botao_1_hitbox.topleft = center_x(self.botao_1), 400

            TELA.blit(self.botao_2, (center_x(self.botao_2), 550)) # Botao 2
            Carta.botao_2_hitbox.topleft = center_x(self.botao_2), 550

            TELA.blit(self.valor_da_carta,(center_x(self.valor_da_carta),300))
            TELA.blit(self.opcoes[0], (center_x(self.opcoes[0]), 430))
            TELA.blit(self.opcoes[1], (center_x(self.opcoes[1]), 580))

            if Carta.botao_1_hitbox.collidepoint(pygame.mouse.get_pos()):
                self.botao_1 = Carta.botao_1_pressionado

                if Click():
                    self.botao_1 = Carta.botao_1_pressionado
                    resposta = [self.resp[0][1],self.resp[2]]
                    if resposta[0] == True:
                        return self.choice(jogador, resposta)
                    else:
                        return resposta



            elif Carta.botao_2_hitbox.collidepoint(pygame.mouse.get_pos()):
                self.botao_2 = Carta.botao_2_pressionado

                if Click():
                    self.botao_2 = Carta.botao_2_pressionado
                    resposta = [self.resp[1][1], self.resp[2]]
                    if resposta[0] == True:
                        return self.choice(jogador, resposta)
                    else:
                        return resposta

            else:
                self.botao_1 = Carta.botao_1
                self.botao_2 = Carta.botao_2
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()



class Jogador(pygame.sprite.Sprite):
    cartas: {}
    nome: object
    jog = 0
    posicao_relativa = [0,0]
    ICONES = [PLAYER,PLAYER_1,PLAYER_2]

    def __init__(self, nome, icon):
        pygame.sprite.Sprite.__init__(self)
        self.jog += 1
        Jogador.jog += 1
        self.contaminado = False
        self.image = Jogador.ICONES[icon]
        self.rect = self.image.get_rect()
        self.nome = nome
        self.cartas = []
        self.posicao = coord_mapa_path[0] # Posicao inicial
        self.mascaras = 0


    def __repr__(self):
        return f"{self.nome}"

    def andar(self, path):
        caminhos = path
        time.sleep(0.5)
        return caminhos.pop(0)

icones_jogadores = pygame.sprite.Group()


#---------- Funções --------------#

def poligono_mapa(coordenadas, scroll): #Constroi os poligonos para interação
    for o in coordenadas:
        pygame.draw.polygon(TELA, (30, 30, 30), [[5 + o[1] + scroll[0], 35 + o[2] + scroll[1]], (60 + o[1] + scroll[0], 2 + o[2] + scroll[1]), (118 + o[1] + scroll[0], 35 + o[2] + scroll[1]), (61 + o[1] + scroll[0], 68 + o[2] + scroll[1])])


def construtor(coordenadas, scroll, crowding):
    for i in coordenadas:
        if i[0] > 0:
            TELA.blit(BLOCK, [i[1] + scroll[0], i[2] + scroll[1]])
            if i[0] in crowding:
                TELA.blit(CROWD, [i[1] + scroll[0]+10, i[2] + scroll[1]-7])
        elif i[0] == 0:
            TELA.blit(BLOCK_0, [i[1] + scroll[0], i[2] + scroll[1]])


def centralizar_camera_personagem(foco):
    x,y = (0,0)
    x += (pos_foco_camera[0] - foco.posicao[1])
    y += (pos_foco_camera[1] - foco.posicao[2])
    return [x,y]


def aglomeracao(rodadas, caminhos): # Adiciona uma quantidade crescente de casas aglomeradas
    if rodadas > 2 and not rodadas % 2 == 0:
        aglomerados = int(rodadas / 2) + 3
        aglomeracoes = []
        for i in range(aglomerados):
            buffer = caminhos[random.randrange(len(caminhos)-1)]
            aglomeracoes.append(buffer[0])
        print(aglomeracoes)

        return aglomeracoes
    else:
        return []


def endgame(Lista_Jogador, Cartas):
    # Se um chegar no fim do mapa (Ganha)
    # Se as cartas acabarem o mais proximo do fim ganha
    # Se um ficar contaminado (Perde)
    # Se os dois ficarem contaminados (Ambos perdem. Game Over)

    def tela_fim_de_jogo (winner = None, mensagem = "Você Foi imunizado"):
        run = True
        while run == True:
            clock.tick(FPS)

            if winner == None:
                while run == True:
                    TELA.blit(badending,(center_x(badending),center_y(badending)))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            pygame.quit()
                break

            TELA.blit(fundo_aviso,(center_x(badending),center_y(badending)))
            parabens = fonte_titulo.render(f"Parabéns{winner}! Você Ganhou!", True, (25, 25, 25))
            TELA.blit(parabens, (center_x(parabens), center_y(parabens)))
            modovitoria = fonte_titulo.render(mensagem, True, (25, 25, 25))
            TELA.blit(modovitoria, (center_x(modovitoria), center_y(modovitoria) + 55))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
        return

    todos_contaminados = True
    contaminado = []
    nao_contaminado = []
    vencedor = False
    for jogador in Lista_Jogador:
        if jogador.contaminado == False:
            todos_contaminados = False
            nao_contaminado.append(jogador)
        else:
            contaminado.append(jogador)


    if todos_contaminados == True:
        tela_fim_de_jogo()


    for jogador in Lista_Jogador:
        if jogador.posicao[0] == coord_mapa_path[-1][0] and jogador not in contaminado:  # O primeiro a chegar no final sem estar contaminado
            vencedor = jogador
            tela_fim_de_jogo(vencedor)

    if len(nao_contaminado) == 1:
        vencedor = nao_contaminado[0]
        tela_fim_de_jogo(vencedor,f"Infelizmente o {contaminado[0]} ficou sem máscara e foi contaminado.")

    if len(Cartas) == 0:
        distancia = 0
        for jogador in Lista_Jogador:
            if jogador.posicao[0] > distancia:
                distancia = jogador.posicao[0] + len(jogador.cartas)
                vencedor = jogador

            elif jogador.posicao[0] == distancia:
                vencedor = "aos dois Jogadores"
        tela_fim_de_jogo(vencedor, "Os dois suportaram até o fim e foram imunizados!")



    pass

def mainloop():
    rodada = 0
    lobby = [Jogador("Jogador Azul", 0), Jogador("Jogador Verde", 1)]
    for i in lobby:
        icones_jogadores.add(i)
    BARALHO = [Carta() for i in range(len(per_resp))]  # Gera o baralho
    print(lobby)
    run = True
    scrolling = [pos_foco_camera[0], pos_foco_camera[1]]  # Todo valor na tela deve obrigatoriamente adicionar esse valor
    while run:
        rodada += 1
        turno = 1
        evento = aglomeracao(rodada,coord_mapa_path)

        for JOGADOR in lobby: # Checa se algum jogador no inicio da rodada está em um campo aglomerado
            if JOGADOR.posicao[0] in evento:
                if JOGADOR.mascaras == 0:
                    JOGADOR.contaminado = True
                else:
                    JOGADOR.mascaras -= 1

        for JOGADOR in lobby:
            turno += 1
            wiggle = 0 # Valor para o movimento da carta
            mover = False
            scrolling = centralizar_camera_personagem(JOGADOR) # Centralizar a camera no jogador no inicio do turno

            index_baralho = random.randrange(len(BARALHO))
            CARTA_TURNO = BARALHO[index_baralho]

            turn = True
            while turn:
                clock.tick(FPS)
                if mover == True:
                    try:
                        JOGADOR.posicao = JOGADOR.andar(path)
                        if JOGADOR.posicao[0] in evento: # Checa se o jogador está tocando em um campo aglomerado
                            if JOGADOR.mascaras == 0:
                                JOGADOR.contaminado = True
                            else:
                                JOGADOR.mascaras -= 1

                    except:
                        mover = False
                        turn = False


                #----------- Comandos e Eventos -----------#

                if Touch(hitbox_carta, pygame.mouse.get_pos()) and mover == False: # Mousehover em puxar carta
                    if wiggle <= 15:
                        wiggle += 5
                    if Click():
                        resposta = CARTA_TURNO.show(JOGADOR)
                        if resposta[0]:
                            mover = True
                            path = [p for p in coord_mapa_path[JOGADOR.posicao[0] : JOGADOR.posicao[0] + resposta[1]]]

                            JOGADOR.cartas.append(BARALHO.pop(index_baralho))

                        else:
                            turn = False
                else:
                    if wiggle > 0:
                        wiggle -= 5


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        turn = False
                    if Click_event(event):
                        for j in lobby:
                            print(f"{j} x e y : ",j.posicao[1] + scrolling[0] + 40, j.posicao[2] + scrolling[1] - 40)

                    if event.type == pygame.KEYDOWN: # Controle de Camera
                        if event.key == pygame.K_SPACE:
                            scrolling = centralizar_camera_personagem(JOGADOR)
                        if event.key == pygame.K_UP:
                            scrolling[1] += 35
                        if event.key == pygame.K_RIGHT:
                            scrolling[0] -= 60
                        if event.key == pygame.K_LEFT:
                            scrolling[0] += 60
                        if event.key == pygame.K_DOWN:
                            scrolling[1] -= 35



                # ----------- Interface Gráfica -----------#
                TELA.fill(CORBACKGROUND)  # refresh do fundo
                poligono_mapa(coord_mapa_path, scrolling)
                construtor(coord_mapa_comp, scrolling, evento)
                for jogador in lobby:
                    TELA.blit(jogador.image, [jogador.posicao[1] + scrolling[0] + 40, jogador.posicao[2] + scrolling[1] - 40])



                # ---------- GUI ------------#
                TELA.blit(BOTAO_CARTA, [center_x(BOTAO_CARTA), HEIGHT - BOTAO_CARTA.get_height() / 2 - wiggle])
                hitbox_carta.topleft = center_x(BOTAO_CARTA), HEIGHT - BOTAO_CARTA.get_height() / 2 - wiggle


                masksize = (MASKGUI.get_width(),MASKGUI.get_height())

                TELA.blit(MASKGUI, (WIDTH - masksize[0] - 15, HEIGHT - masksize[1] - 15))
                info_mask = fonte.render(f"{JOGADOR.mascaras}  Máscaras", True, (25, 25, 25))
                TELA.blit(info_mask, (WIDTH - masksize[0]/2 - 65, HEIGHT - masksize[1] + 95))
                indicador_mascara = fonte_info.render(f"Mascaras:", True, (255, 255, 255))
                posx = 190
                TELA.blit(indicador_mascara, (10, center_y(indicador_mascara) - posx))
                for i in lobby:
                    posx -= 25
                    indicador_mascara = fonte_info.render(f"{i.nome}: {i.mascaras}", True, (255, 255, 255))
                    TELA.blit(indicador_mascara, (10, center_y(indicador_mascara) - posx))

                indicador_turno = fonte_titulo.render(f"Rodada {rodada}: {JOGADOR.nome}", True, (255, 255, 255))
                TELA.blit(indicador_turno, (center_x(indicador_turno), 60))

                indicador_evento = fonte_titulo.render(f"Aglomerações! Não esqueça da sua máscara", True, (255, 255, 255))
                if rodada > 2 and not rodada % 2 == 0: # se a rodada for maior que 2 e impar alertar sobre aglomeracoes
                    TELA.blit(indicador_evento, (center_x(indicador_evento), 27))
                endgame(lobby,BARALHO)

                pygame.display.update()

            if run == False:
                print("Closing")
                break

    pygame.quit()



# ----------------------------------------------------#
if __name__ == "__main__":
    mainloop()