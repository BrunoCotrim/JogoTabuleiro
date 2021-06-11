import pygame
import pygame.font
import  main

pygame.init()
def quantidadejogador(quant):
     op = quant
     print (op)
     return op


def quantidadejogador2(quant):
    op = quant
    print(op)
    return op


preto = (0,0,0)
def text_botoes(texto, fonte): # cria os textos dos botões
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()

letras = pygame.image.load('menu.jpeg')
virusvacina = pygame.image.load('vacina.jpeg')

LARGURA, ALTURA = 1024, 740
display = pygame.display.set_mode([LARGURA, ALTURA]) # criando janela
pygame.display.set_caption("Menu Principal") # nome da janela
size = [110,50]

display.fill([0,0,0])  # preenchendo a janela de cor
display.blit(letras, (main.center_x(letras),-280))
display.blit(virusvacina, (main.center_x(virusvacina),170))

pos_1 = [LARGURA/2 - size[0]/2 ,ALTURA/2 - size[1]/2+50]
botao1 = pygame.Rect(pos_1,size)
pygame.draw.rect(display,[36, 128, 20], botao1)
textobotao = pygame.font.Font('freesansbold.ttf', 18)
textSurf, textRect = text_botoes("Iniciar", textobotao)
textRect.center = ((pos_1[0] + size[0]/2), (pos_1[1] + size[1]/2))
display.blit(textSurf, textRect)
pos_2 = [LARGURA/2 - size[0]/2 ,ALTURA/2 - size[1]/2 + 120]
botao2 = pygame.Rect(pos_2,size)
pygame.draw.rect(display, [36, 128, 20], botao2)
textobotao = pygame.font.Font('freesansbold.ttf', 18)
textSurf, textRect = text_botoes("Sair", textobotao)
textRect.center = ((pos_2[0] + size[0]/2), (pos_2[1] + size[1]/2))
display.blit(textSurf, textRect)




gameLoop = True

if __name__ == "__main__":
     while gameLoop:


          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    gameLoop = False
               if pygame.mouse.get_pressed()[0]:
                    if botao2.collidepoint(pygame.mouse.get_pos()):
                         gameLoop = False

                    elif botao1.collidepoint(pygame.mouse.get_pos()):
                        main.mainloop()





                          

          pygame.display.update()









