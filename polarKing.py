import pygame, sys
from pygame.locals import *
import random

#definindo as cores que vao ser usados no jogo (R, G, B)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (0, 200, 255)
YELLOW = (255, 255, 0)
PURPLE = (170, 0, 225)
colours = [GREEN, RED, LIGHTBLUE, YELLOW, PURPLE]

#iniciando as variaveis
score = 0
levelNum = 0
dificuldade = 0

pressed = False #a variavel pressed quando for verdadeira vai comecar o jogo
replay = True #A variável replay é usada como uma condição para manter o loop principal do jogo em execução. (Ja começa como verdadeiro, para rodar o programa)
introDone = False # Indica se a introdução foi concluída
startDone = False # Indica se a preparação inicial foi concluída
startOutput = False # Indica se o inicio foi exibida
gameStart = False # Indica se o jogo começou
lançarBarril = False # Indica se o urso está prestes a lançar um barril
puloEsquerda = False # Indica se o pinguim está pulando para a esquerda
puloDireita = False # Indica se o pinguim está pulando para a direita
puloParado = False # Indica se o pinguim esta pulando parado
dano = False #Indica se o pinguim foi atingido
morte = False #Indica quando o pinguim morre, comecando no falso
gameDone = False #indica quando o jogo e fechado
winGame = False #indica quando o usuario ganha o jogo
winLevel = False #Indica o level do usuario ao ganhar o jogo
scoreWin = False #indica o score que ganhou
direction = False #indica a direcao do pinguim
winGameSceneOutput = False
winGameSceneDone = False

#informando as posicoes das plataformas, (X, Y)
plataformasX = [55, 55, 51, 60, 56, 56, 56]
plataformasY = [9, 10, 8, 9, 11, 9, 9, 11]
platNum = 0 #iniciando com o numeros de plataformas

#inicializando as variaveis do urso
ursoClimb = 0 
climbCount = 15
platNum = 0
ursoPuloX = 378
ursoPuloY = 172
ursoPuloYnum = 0

#inicializando as variaveis do pinguim
pinguimX = 150
pinguimY = 720

#inicializando as variaveis geral do jogo
addPulo = -7
puloCount = 0
puloPoint = 0
deathCount = 0
vidas = 2

#incializando as variaveis do barril
barrilX = [] #variavel para guardar a posicao X do barril
barrilY = [] #variavel para guardar a posicao Y do barril
lançarCountdown = 0
barrilDirection = [] #variavel para guardar a direcao que o barril esta indo
fall = [] #variavel para guardar quando o barril esta em queda
fallCount = []
barrilLeft = [] #variavel para guardar quando o barril esta indo para a esquerda
barrilRight = [] #variavel para guardar quando o barril esta indo para a direita

platInclineX = [100, 140, 190, 240, 280, 330, 380, 430, 480, 530, 570, 620, 670, 720] #lista guardando as inclinacoes das plataformas na posicao X
inclineCount = 0 #inicializando a variavel de contagem de inclinacao

#representam as coordenadas x e y do ponto inferior esquerdo de cada escada
ladderX1 = [295, 605, 295, 345, 345, 150, 245, 385, 600, 600, 245, 150, 265, 265, 315, 555, 555, 600, 440, 320]
ladderX2 = [305, 610, 310, 350, 350, 160, 255, 400, 610, 610, 255, 160, 280, 280, 325, 565, 565, 610, 450, 335]

# representam as coordenadas x e y do ponto superior direito de cada escada.
ladderY1 = [710, 635, 617, 610, 526, 538, 522, 423, 506, 435, 414, 338, 409, 332, 309, 314, 417, 241, 154, 232]
ladderY2 = [720, 705, 657, 620, 571, 608, 532, 523, 511, 475, 464, 408, 414, 382, 329, 369, 432, 311, 232, 272]

# indica se uma escada permite subir completamente (True) ou não (False)
fullLadderUp = [False, True, True, False, True, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True]
#indica se uma escada permite descer completamente (True) ou não (False)
fullLadderDown = [True, True, False, True, False, True, True, True, True, False, False, True, True, False, True, False, True, True, True, False]

#sao usadas para verificar se o personagem principal atingiu um limite em determinadas posições na tela
leftLimitesY = [541, 341]
rightLimitesY = [638, 438, 244]

barrilLadderX = [320, 610, 560, 280, 160, 250, 400, 610, 350, 160, 300, 610] #Contém as coordenadas x das posições iniciais dos barris em relação às escadas
barrilLadderY1 = [243, 252, 326, 270, 350, 428, 437, 449, 535, 547, 627, 645] #Contém as coordenadas y superiores das escadas onde os barris podem aparecer
barrilLadderY2 = [343, 322, 446, 344, 420, 538, 527, 519, 625, 617, 727, 715] #Contém as coordenadas y inferiores das escadas onde os barris podem aparecer
barrilAdjust = [-2, 1, -1, 4, 2, 3, 5, 1, 5, 1, 4, 1] #Contém ajustes nas coordenadas x dos barris para posicionar corretamente os barris ao longo das escadas

#definindo as imagens
title = pygame.image.load("sprites//title-tela.png")
start = pygame.image.load("sprites//start.png")
winScreen = pygame.image.load("sprites//win-tela.png")
winScreen = pygame.transform.scale(winScreen, (800, 800))
gameOverScreen = pygame.image.load("sprites//GameOver.png")
gameOverScreen = pygame.transform.scale(gameOverScreen,(800, 800))
vida = pygame.image.load("sprites//vida.png")

fundo = pygame.image.load("sprites//fundo.png")

pinguimLeft = pygame.image.load("sprites//pinguim-left.png")
pinguimRight = pygame.image.load("sprites//pinguim-right.png")
runLeft = pygame.image.load("sprites//pinguim-runleft.png")
runRight = pygame.image.load("sprites//pinguim runRight.png")
pinguimPuloLeft = pygame.image.load("sprites//pinguim-left.png")
pinguimPuloRight = pygame.image.load("sprites//pinguim-right.png")
pinguimClimb1 = pygame.image.load("sprites//pinguim-Climb1.png")
pinguimImage = pinguimRight

ursoForward = pygame.image.load("sprites//polar1.png")
ursoForward = pygame.transform.scale(ursoForward, (125*2, 92*2))
ursoLeft = pygame.image.load("sprites//polar1.png")
ursoLeft = pygame.transform.scale(ursoLeft, (125*2, 92*2))
ursoRight = pygame.image.load("sprites//polar2.png")
ursoRight = pygame.transform.scale(ursoRight, (125*2, 92*2))
ursoImage = ursoForward

barrilStack = pygame.image.load("sprites//barril-stack.png")
barrilDown = pygame.image.load("sprites//barril-baixo.png")
barril1 = pygame.image.load("sprites//barril1.png")
barril2 = pygame.image.load("sprites//barril2.png")
barril3 = pygame.image.load("sprites//barril3.png")
barril4 = pygame.image.load("sprites//barril4.png")
barrilSequence = [barril1, barril2, barril3, barril4]
barrilPic = []

brokenHeart = pygame.image.load("sprites//broken-heart.png")
fullHeart = pygame.image.load("sprites//full-heart.png")

clock = pygame.time.Clock() #para controlar a taxa de quadros do jogo

def collide() -> bool: #funcao para verificar quando o pinguim colide com o barril, retornando em tipo booleano
    global dano #tornando a variavel dano em global
    
    #Percorre todos os barris da lista, coordenadas X
    for i in range(0, len(barrilX)):
        #Se a imagem do pinguim tocar em qualquer lugar da imagem do barril, dano e True. 
        #(20 = largura do pinguim) (26 = largura do barril) (30 = altura do pinguim) (20 = altura do barril)
        if pinguimX+20 >= barrilX[i] and pinguimX <= barrilX[i]+26 and pinguimY+30 >= barrilY[i] and pinguimY <= barrilY[i]+20:
            dano = True
            
    return dano #retorna dano em valor booleano como especificado na funcao

def ladderCheck():  # Função para checar se o pinguim está em uma escada
    global pinguimY  # Torna a variável pinguimY global
    
    # Declaração de variáveis
    upLadder = False
    downLadder = False
    moveSides = True
    
    # Percorre todas as escadas
    for i in range(0, len(ladderX1)): #percorre a lista da escada com as coordenadas X
        # Se o pinguim estiver dentro da área de uma escada, ele pode se mover para cima, para baixo e para os lados
        #Essa condição verifica se as coordenadas do pinguim (pinguimX e pinguimY) estão dentro da área definida por uma escada específica (determinada pelos índices i)
        if pinguimX >= ladderX1[i] and pinguimX <= ladderX2[i] and pinguimY >= ladderY1[i] and pinguimY <= ladderY2[i]:
            downLadder = True #indica que o pinguim pode se mover para baixo na escada
            upLadder = True #indica que o pinguim pode se mover para cima na escada
            moveSides = False #indica que o pinguim não pode se mover para os lados enquanto estiver na escada
            
            # Se o pinguim estiver no topo de uma escada, ele não pode se mover para cima mais
            if pinguimY == ladderY1[i]:
                upLadder = False
                
                # Se a escada não estiver quebrada subindo, ele pode se mover para os lados quando estiver no topo
                if fullLadderUp[i]:
                    moveSides = True      
            
            # Se o pinguim estiver na parte inferior da escada, ele não pode se mover para baixo mais 
            if pinguimY == ladderY2[i]:
                downLadder = False
                
                # Se a escada não estiver quebrada descendo, ele pode se mover para os lados quando estiver na parte inferior
                if fullLadderDown[i]:
                    moveSides = True
        
        # Sai do loop para parar de verificar em qual escada o pinguim está, porque o computador já encontrou
        if upLadder or downLadder:
            break
            
    return upLadder, downLadder, moveSides


# incline - move o pinguim para cima para que ele possa subir em uma inclinação ao andar/pular na plataforma
def incline(y, x, direction, objectt):
    global inclineCount #tornando essa variavel em global
    
    # se o objeto estiver na plataforma inferior
    if y <= 720 and y >= 657:
        startNum = 6
        endNum = len(platInclineX) - 1
        move = 3
        
    # se o objeto estiver na segunda ou quarta plataforma
    elif (y <= 638 and y >= 553) or (y >= 353 and y <= 438):
        startNum = 0
        endNum = len(platInclineX) - 2
        move = -3
        
    # se o objeto estiver na terceira ou quinta plataforma
    elif (y <= 541 and y >= 456) or (y <= 341 and y >= 256):
        startNum = 1
        endNum = len(platInclineX) - 1
        move = 3
        
    # se o objeto estiver na plataforma superior
    elif y <= 245 and y >= 149:
        startNum = 8
        endNum = len(platInclineX) - 2
        move = -3
    
    # se não estiver em uma plataforma (em uma escada)
    else:
        startNum = 0
        endNum = 0
        move = 0
    
    # percorre a lista platIncline, com uma variedade de números diferentes dependendo da plataforma em que o objeto está
    for i in range(startNum, endNum):
        
        # se o objeto tiver o mesmo x que um dos pontos de inclinação x, o objeto inclinará para cima ou para baixo
        if x == platInclineX[i]:
            
            # se o objeto for o pinguim e ele estiver pulando para a esquerda ou para a direita, acompanhe quantas inclinações ele passou enquanto pulava
            if (puloEsquerda or puloDireita) and objectt == "pinguim":
                inclineCount = inclineCount + 1    
            
            # caso contrário, descubra em qual direção ele está se movendo
            else:
                # se for para a direita, subtrai move de y
                if direction == "right":
                    y = y - move
                # se for para a esquerda, adiciona move a y                  
                elif direction == "left":
                    y = y + move
    
    # retorna move se a função for para o pinguim ao pular
    if (puloEsquerda or puloDireita) and objectt == "pinguim":
        return move
    # caso contrário, retorna o novo valor de y
    else:
        return y


# limites - verifica todos os limites do pinguim e dos barris
def limite(x, y):
    # declara variáveis
    left = True
    right = True
    
    # se x estiver nessa faixa, o pinguim atingiu um possível limite à esquerda dele
    if x <= 105 and x >= 96:
        # percorre as coordenadas y dos limites à esquerda
        for i in range(0, len(leftLimitesY)):
            
            # se o pinguim estiver nessa faixa de limite y também, left é False e o pinguim não pode se mover para a esquerda
            if y <= leftLimitesY[i] and y >= leftLimitesY[i] - 49:
                left = False
                
    # se x estiver nessa faixa, o pinguim atingiu um possível limite à direita dele            
    elif x >= 660 and x <= 669:
        # percorre as coordenadas y dos limites à direita
        for i in range(0, len(rightLimitesY)):
            
            # se o pinguim estiver nessa faixa de limite y também, right é False e o pinguim não pode se mover para a direita
            if y <= rightLimitesY[i] and y >= rightLimitesY[i] - 49:
                right = False
                     
    return left, right

# startScreen - exibe a tela inicial
def startScreen():
    # blit da imagem na tela
    screen.blit(start, (48, 0))

# background - exibe o nível e a pilha de barris
def background():
    # blit das imagens na tela
    screen.blit(fundo, (31, -14))
    screen.blit(barrilStack, (60, 188))

# urso - exibe o personagem urso na tela
def urso():
    # blit da imagem na tela
    screen.blit(ursoImage, (130, 176))

# pinguim - exibe o personagem pinguim na tela
def pinguim():
    # blit da imagem na tela
    screen.blit(pinguimImage, (pinguimX, pinguimY))

# barril - exibe todos os barris na tela
def barril():
    # percorre todos os barris para encontrar as informações de cada barril e exibi-los na tela
    for i in range(0, len(barrilPic)):
        screen.blit(barrilPic[i], (barrilX[i], barrilY[i]))

# pinguimVidas - exibe a representação visual de quantas vidas o pinguim tem restantes
def pinguimVidas():
    # percorre todas as vidas que você tem restantes
    for i in range(0, vidas):
        # utiliza o comando blit para exibir as imagens, adicionando 20 à coordenada y a cada iteração do loop
        screen.blit(vida, (60 + i * 20, 100))
    
def win():
    
    background() #chama a funcao das imagens de fundo
    screen.blit(pinguimLeft, (440, 150)) #faz o pinguim nessas coordenadas
    
    # se urso subiu menos que 30 pixels
    if ursoClimb <= 30:
        screen.blit(fullHeart, (386, 130)) #Se a condição for verdadeira, blita uma imagem de coração inteiro
    # caso contrário, apenas blit de um coração quebrado
    else:
        screen.blit(brokenHeart, (387, 130))
    
    # se o jogo não foi ganho, alterna entre duas imagens para blit
    if not winGame: #verifica se winGame e falso
        if ursoClimb % 30 == 0: #se subida do urso for um múltiplo de 30, blita uma imagem de ursoImage
            screen.blit(ursoImage, (240 - moveOver1, 160 - ursoClimb))
        else:  
            screen.blit(ursoImage, (240 - moveOver2, 160 - ursoClimb))
            
    # caso contrário, apenas blit do urso
    else:
        urso()

# end - exibe o final do jogo
def end(endScreen):
    screen.blit(endScreen, (0, 30))

#redraw_screen - função que redesenha a tela
def redraw_screen():
    #variaveis global
    global gameStart
    global gameDone
    global winGameSceneDone
    global startDone
    global startOutput
    
    # preenchendo a cor da tela
    screen.fill(BLACK)

    # se o jogo estiver concluído, exibe a tela final e a pontuação do usuário
    if gameDone:
        # chama funções de desenho
        end(gameOverScreen)
    
    # se winGame for True, vai para as sequências de vitória do jogo
    elif winGame:
        # se isso for verdadeiro, blit das imagens para mostrar o momento em que urso é derrotado
        if winGameSceneOutput:
            # chama funções de desenho
            win()
            pinguimVidas()
        
        elif winGameSceneDone:
            # chama funções de desenho
            end(winScreen)
    
    # caso contrário, o usuário ainda não ganhou ou perdeu o jogo
    else:
        # se pressed for False, a tela de título está sendo blitada
        if pressed == False:
            screen.blit(title, (0, 0))
        
        # se pressed for True e introDone, blit da sequência de introdução
        elif pressed and introDone == False:
            # chama funções de desenho
            pinguimVidas()
        
        # se a introdução estiver concluída e o jogo ainda não começou, blit da tela de início
        elif introDone == True and gameStart == False:
            # chama funções de desenho
            startScreen()
            pinguimVidas()
            
            # estabelecendo que o início está concluído redefinindo as variáveis
            startOutput = True
            startDone = True
        
        # se o jogo começou e o nível não foi vencido ou o pinguim morreu, blit das imagens normais do jogo
        elif (gameStart and winLevel == False):
            # chama funções de desenho
            background()
            urso()
            pinguim()
            pinguimVidas()
            
            # blitando barris se scoreWin e morte for False
            if scoreWin == False and morte == False:
                barril()
        
        # se o usuário vencer o nível, exibe a sequência de vitória
        elif winLevel:
            # chama funções de desenho
            win()
            pinguimVidas()
     
    # atualizando
    pygame.display.update()

# Inicia todo o jogo se o usuário desejar reiniciar continuamente
pygame.init()

# Carregamento de arquivos de som para diferentes eventos no jogo
walk = pygame.mixer.Sound("sons\\walking.wav")  # Som do personagem caminhando
pulo = pygame.mixer.Sound("sons\\jump.wav")        # Som do personagem pulando
intro = pygame.mixer.Sound("sons\\intro1.wav")   # Som da introdução do jogo
death = pygame.mixer.Sound("sons\\death.wav")     # Som da morte do personagem
bac = pygame.mixer.music.load("sons\\bacmusic.wav")  # Carrega a música de fundo

# Variável para contar o número de mortes no jogo
death_cnt = 0

# Inicia a criação de um programa gráfico

# Configurações iniciais da tela do jogo
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome da janela aberta
pygame.display.set_caption('Polar King')

# Início do jogo
inPlay = True

# Reprodução contínua da música de fundo em loop infinito
pygame.mixer.music.play(-1)

while replay:

    # Continua a fazer loop e mantém a interface gráfica em execução enquanto inPlay é verdadeiro
    while inPlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        introDone = True

        #Se gameStart for verdadeiro, o jogo começou
        if gameStart:
            
            # Se scoreWin e winLevel forem falsos, verifica colisões
            if scoreWin == False and winLevel == False:
                dano = collide()
            
            #Verifica se pinguim teve dano em uma borda à esquerda ou à direita 
            moveLeft, moveRight = limite(pinguimX, pinguimY)
            
            #Se dano for falso, pinguim não teve dano de um barril e o jogo continua normalmente
            if dano == False:
                
                #Verifica se o pinguim está em uma escada e se ele pode subir, descer ou se mover lateralmente
                upLadder, downLadder, moveSides = ladderCheck()
                
                #Se o pinguim atingir um valor de y menor ou igual a 154, ele venceu o jogo, que é a parte superior
                if pinguimY <= 154:
                    #resetando as variaveis
                    winLevel = True
                    ursoClimb = -15
                    climbCount = 15
                    pinguimX = 150
                    pinguimY = 720
                    pinguimImage = pinguimRight
                
                #Se o pinguim está pulando, altera valores de x e/ou y conforme necessario
                if puloEsquerda or puloDireita or puloParado:
                    
                    #Mantém o controle de quantos pulos
                    puloCount += 1
                    
                    #Altera coordenadas y, quando pula
                    pinguimY += addPulo
                    
                    #Quando puloCount é 7, faz o pinguim descer, alterando o número que ele sobe/desce
                    if puloCount == 7:
                        addPulo = 7
                    
                    #Se puloCount é 14, o pinguim desce
                    if puloCount == 14:
                        
                        #Se o pinguim estava virado para a direita, muda a imagem de volta para ele virado para a direita, e altera o valor y se ele pulou sobre algumas inclinações
                        if direction == "right":
                            pinguimImage = pinguimRight
                            pinguimY = pinguimY - move*inclineCount
                        #Se o pinguim estava virado para a esquerda, muda a imagem de volta para ele virado para a esquerda, e altera o valor y se ele pulou sobre algumas inclinações
                        else:
                            pinguimImage = pinguimLeft
                            pinguimY = pinguimY + move*inclineCount
                            
                        #resetando as variaveis
                        addPulo = -7
                        puloCount = 0
                        puloPoint = 0
                        inclineCount = 0
                        
                        puloEsquerda = False
                        puloDireita = False
                        puloParado = False
                        
                    #Se o pinguim atingiu uma borda lateral, não adicione aos valores de x
                    if pinguimX != 60 and pinguimX != 710 and (pinguimX != 320 or pinguimY >= 232):
                        #Verifica quantas inclinações o pinguim pulou e se deve mover para cima ou para baixo quando ele pousa
                        move = incline(pinguimY, pinguimX, direction, "pinguim")
                        
                        #Se o pinguim está pulando para a esquerda e pode se mover para a esquerda, subtrai 5 de suas coordenadas x
                        if puloEsquerda and moveLeft:
                            pinguimX = pinguimX - 5
                        #Se o pinguim está pulando para a direita e pode se mover para a direita, soma 5 de suas coordenadas x
                        elif puloDireita and moveRight:
                            pinguimX = pinguimX + 5
                    
                
                # Se scoreWin for falso, mantém os barris rolando
            
                if not scoreWin:
                    
                    # Passa por todos os barris
                    for i in range(0, len(barrilPic)):
                        # Se o barril atingir o final da estrutura, faz o barril desaparecer da tela
                        if barrilX[i] <= 31:
                            barrilX[i] = -30
                            barrilY[i] = -30
                        
                        # Se o barril não estiver caindo, verifica se ele está
                        if not fall[i]:
                            #verificar se o barril na posição i pode se mover para a esquerda ou para a direita, considerando um deslocamento vertical de 15 pixels 
                            barrilLeft[i], barrilRight[i] = limite(barrilX[i], barrilY[i] - 15) 
                            
                            # Reseta a variável se o barril tiver causado dano a uma plataforma e não puder se mover para a esquerda ou para a direita
                            if not barrilLeft[i] or not barrilRight[i]:
                                fall[i] = True

                        #verifica em qual plataforma o barril está para determinar a direção em que está indo
                        if (barrilY[i] <= 255 and barrilY[i] >= 243) or (barrilY[i] <= 452 and barrilY[i] >= 415) or (barrilY[i] <= 648 and barrilY[i] >= 611):
                            barrilDirection[i] = "right"
                            
                        elif (barrilY[i] <= 353 and barrilY[i] >= 317) or (barrilY[i] <= 550 and barrilY[i] >= 513) or (barrilY[i] <= 731 and barrilY[i] >= 709):
                            barrilDirection[i] = "left"
                        
                        #se o barril não estiver em uma escada, está rolando ou caindo
                        if barrilPic[i] != barrilDown:
                            
                            #se o barril não estiver caindo, está rolando para a esquerda ou direita
                            if fall[i] == False:
                                #move o barril para a esquerda ou direita com base em sua direção
                                if barrilDirection[i] == "right":
                                    barrilX[i] = barrilX[i] + 10
                                else:
                                    barrilX[i] = barrilX[i] - 10
                                
                                # Ajusta a posição y do barril levando em consideração a inclinação do cenário
                                barrilY[i] = incline(barrilY[i] - 11, barrilX[i], barrilDirection[i], "barril")

                                # Compensa a subtração inicial de -11 adicionando 11 à posição y ajustada
                                barrilY[i] = barrilY[i] + 11

                            # Caso contrário, o barril está no processo de cair
                            else:
                                # Adiciona um para acompanhar quanto tempo ele está caindo
                                fallCount[i] = fallCount[i] + 1
                                
                                # Se o barril está caindo no lado esquerdo, subtrai x por 5
                                if barrilLeft[i] == False:
                                    barrilX[i] = barrilX[i] - 5
                                
                                # Se está caindo pelo lado direito, adiciona x por 5
                                elif barrilRight[i] == False:
                                    barrilX[i] = barrilX[i] + 5
                                
                                # Altera y por 7 a cada iteração
                                barrilY[i] = barrilY[i] + 7
                                
                                # Se a contagem atingiu 8, interrompe a queda e reseta os valores para a próxima vez
                                if fallCount[i] == 8:
                                    # Ajusta para garantir que ele pouse na plataforma correta
                                    barrilY[i] = barrilY[i] + 6
                                    
                                    # Reseta as variáveis
                                    fallCount[i] = 0
                                    fall[i] = False
                                    barrilLeft[i] = True
                                    barrilRight[i] = True

                            
                            #Muda a imagem do barril a cada iteração
                            #Se a imagem do barril estiver no índice 3, muda para o índice 0
                            if barrilPic[i] == barrilSequence[3]:
                                barrilPic[i] = barrilSequence[0]
                                
                            #se nao, muda para o próximo número na lista
                            else:
                                for j in range(0, len(barrilSequence)-1):
                                    if barrilPic[i] == barrilSequence[j]:
                                        barrilPic[i] = barrilSequence[j+1]
                        
                        #Se a imagem do barril for barril para baixo, o barril está descendo uma escada e adiciona 10 ao valor de y a cada iteração
                        else:
                            barrilY[i] = barrilY[i] + 10
                        
                        #Percorre todas as coordenadas de escada para os barris
                        for j in range(0, len(barrilLadderX)):
                            #Se as coordenadas x e y do barril forem iguais a barrilLadderX[j] e barrilLadderY[j], respectivamente, usa um número aleatório para decidir se o barril deve descer ou não
                            if barrilX[i] == barrilLadderX[j] and barrilY[i] == barrilLadderY1[j]:
                                barrilChoice = random.randint(0, 1)
                                
                                #Se o número aleatório escolhido for 0, a imagem e coordenadas do barril serão redefinidas
                                if barrilChoice == 0:
                                    barrilPic[i] = barrilDown
                                
                                    barrilX[i] = barrilX[i] - 2
                            
                            #Se o barril atingir o final de uma escada, redefina as variáveis de volta
                            if barrilX[i]+2 == barrilLadderX[j] and barrilY[i] == barrilLadderY2[j]:
                                barrilPic[i] = barrilSequence[0]
                                barrilX[i] = barrilX[i] + 2
                                
                                #Isso garante que, quando descer, aterrissará corretamente na plataforma em vez de 5 pixels muito alta, já que os barris se movem 10 pixels de cada vez
                                barrilY[i] = barrilY[i] + barrilAdjust[j]
                    
                    #Se lançarBarrel for falso, obtenha um número aleatório para decidir se o urso lançará outro barril ou não        
                    if lançarBarril == False:
                        #Após cada nível, o intervalo será menor, o que significa uma maior chance de lançar barris
                        ursoChoice = random.randint(0, 50-dificuldade)
                        
                        #Se o número for 0, redefina as variáveis para lançar o barril
                        if ursoChoice == 0:
                            ursoImage = ursoLeft
                            lançarBarril = True
                        #se nao, nao lance nenhum barril 
                        else:
                            ursoImage = ursoForward
                            lançarBarril = False
                    
                    #Se lançarBarrel for verdadeiro, faça essas alterações
                    if lançarBarril:
                        
                        #Adiciona para dar o urso algum tempo para pegar o barril
                        lançarCountdown = lançarCountdown + 1
                        
                        #Se lançarCountdown for 20, crie um novo barril
                        if lançarCountdown == 20:
                            #resetando a variavel do urso
                            ursoImage = ursoRight
                            
                            #Declaração das novas informações do barril
                            barrilX.append(250)
                            barrilY.append(243)
                            barrilDirection.append("right")
                            barrilPic.append(barril1)
                            fall.append(False)
                            fallCount.append(0)
                            barrilLeft.append(True)
                            barrilRight.append(True)
                            
                        #Se lançarCountdown atingir 40, redefina as variáveis para quando o urso não estava lançando barril
                        if lançarCountdown == 40:
                            lançarCountdown = 0
                            ursoImage = ursoForward
                            lançarBarril = False
            
            #se nao, pinguim sofre dano, inicia as sequências de morte
            else:
                #Se a morte não foi concluída
                if not pygame.mixer.get_busy():
                    pygame.mixer.Sound.play(death)

                if morte == False:
                    #Move as coordenadas y do pinguim morto para baixo para garantir que ele repouse onde estavam seus pés, não onde estava sua cabeça
                    if deathCount == 0:
                        pinguimY = pinguimY + 10
                    
                    deathCount = deathCount + 1
                    
                    #quando a contagem atinge 60, o curto atraso acabou, redefine variáveis e perde uma vida
                    if deathCount == 60:
                        morte = True
                        deathCount = 0 
                        vidas -= 1

                    
                #Se a morte é verdadeira, redefina as variáveis para recomeçar no início do nível novamente
                else:
                    startDone = False
                    gameStart = False
                    lançarBarril = False
                    morte = False
                    dano = False
                    puloEsquerda = False
                    puloDireita = False
                    puloParado = False
                    barrilX = []
                    barrilY = []    
                    barrilPic = []
                    lançarCountdown = 0
                    barrilDirection = []
                    fall = []
                    fallCount = []
                    barrilLeft = []
                    barrilRight = []
                    inclineCount = 0
                    puloPoint = 0
                    pinguimX = 150
                    pinguimY = 720
                    addPulo = -7
                    puloCount = 0
                    direction = "right"
                    pinguimImage = pinguimRight
                
                if vidas < 0: #se vidas for menor que 0, quer dizer que o usuario perdeu
                    gameDone = True
        
        #Se você vencer o nível, inicie os processos de vitória de nível
        if winLevel:
            #Se o número do nível for 5 ou scoreWin for verdadeiro, redefina os valores para exibir as imagens corretas em redraw_screen
            if levelNum == 5:
                #Se isso for falso, redefina os valores para iniciar o final do jogo
                if winGameSceneDone == False:
                    winGameSceneOutput = True
                
                #se nao, continue para o proximo nivel
                gameStart = False
                winGame = True
            
            #se nao, continue para o proximo nivel
            else:
                
                #o urso sobe
                ursoClimb = ursoClimb + climbCount
                
                #Se o urso subir 15 pixels, adicione 250 à pontuação e aguarde um tempo
                if ursoClimb == 15:
                    score = score + 250
                    pygame.time.delay(1000)
                
                if ursoClimb <= 30:
                    moveOver1 = 0
                    moveOver2 = 0
                    
                    #Ajusta a imagem para que ele suba suavemente
                    moveOver1 = 13
                    moveOver2 = 35
                
                #Se urso subiu 150 pixels, redefina variáveis para o próximo nível
                if ursoClimb == 150: 
                    winLevel = False
                    introDone = False
                    startDone = False
                    gameStart = False
                    lançarBarril = False
                    puloEsquerda = False
                    puloDireita = False
                    puloParado = False
                    dano = False
                    barrilX = []
                    barrilY = []    
                    barrilPic = []
                    barrilDirection = []
                    fall = []
                    fallCount = []
                    barrilLeft = []
                    barrilRight = []
                    inclineCount = 0
                    ursoClimb = 0
                    platNum = 0
                    climbCount = 15
                    ursoPuloX = 378
                    ursoPuloY = 172
                    ursoPuloYnum = 0
                    addPulo = -7
                    puloCount = 0
                    direction = "right"
                    
                    #para tornar o próximo nível mais difícil
                    dificuldade += 5
            
        #Procura pelo evento (ação de usar o teclado)
        pygame.event.get()
        
        # O método get_pressed() gera uma lista True/False para o status de todas as teclas
        keys = pygame.key.get_pressed()
        
        #Procura pela tecla Esc ser pressionada
        if keys[pygame.K_ESCAPE]:
            
            #resetando as variaveis, para sair do programa
            inPlay = False
            replay = False
        
        #Procura pela tecla de espaço ser pressionada para definir pressed como True e iniciar o jogo
        if keys[pygame.K_SPACE]:
            pressed = True
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(intro)

        #Deve satisfazer todas essas condições para que pressionar as teclas esquerda, direita, cima, baixo, espaço (para pular) e Enter, para que faça alguma coisa
        if (gameStart and puloEsquerda == False and puloDireita == False and puloParado == False and winLevel == False and dano == False) or gameDone or winGame:      
            
            #Procura pela tecla de seta para a esquerda ser pressionada
            #(pinguimX != 320 or pinguimY > 232): Verifica se a posição do pinguim não está no meio da escada (X != 320) ou se o pinguim está acima de uma certa altura (Y > 232)
            #Verifica se a posição do pinguim não está no limite esquerdo (X != 60).
            if keys[pygame.K_LEFT] and moveSides and (pinguimX != 320 or pinguimY > 232) and moveLeft and pinguimX != 60:
                #Altera a coordenada y do pinguim para inclinar para cima/baixo com a inclinação
                pinguimY = incline(pinguimY, pinguimX, direction, "pinguim")
                # Se a direcao do pinguim for left, subtrai X por 5
                if direction == "left":
                    pinguimX = pinguimX - 5
                
                #Se a imagem para o pinguim for pinguimLeft, muda para runLeft
                if pinguimImage == pinguimLeft:
                    pinguimImage = runLeft
                    if not pygame.mixer.get_busy():
                        pygame.mixer.Sound.play(walk)


                #se nao, muda para pinguimLeft
                else:
                    pinguimImage = pinguimLeft
                    
                #Se a barra de espaço for pressionada enquanto a seta para a esquerda também estiver sendo pressionada, puloEsquerda é True e muda a imagem
                if keys[pygame.K_SPACE]:
                    puloEsquerda = True
                    pinguimImage = pinguimPuloLeft
                    # if not pygame.mixer.get_busy():
                    pygame.mixer.Sound.stop(walk)
                    pygame.mixer.Sound.play(pulo)
                
                direction = "left"

            #Procura pela tecla de seta para a direita ser pressionada 
            elif keys[pygame.K_RIGHT] and moveSides and moveRight and pinguimX != 710:
                #Altera a coordenada y do pinguim para inclinar para cima/baixo com a inclinação
                pinguimY = incline(pinguimY, pinguimX, direction, "pinguim")
                
                #Se o pinguim já estiver virado para a direita, adiciona 5 a pinguimX
                if direction == "right":
                    pinguimX = pinguimX + 5
                #Se a imagem para o pinguim for pinguimRight, muda para runRight
                if pinguimImage == pinguimRight:
                    pinguimImage = runRight
                    if not pygame.mixer.get_busy():
                        pygame.mixer.Sound.play(walk)
                #se nao, muda para pinguimRight
                else:
                    pinguimImage = pinguimRight
                
                #se a barra de espaço for pressionada enquanto a seta para a direita também estiver sendo pressionada, puloDireita é True e muda a imagem
                if keys[pygame.K_SPACE]:
                    puloDireita = True
                    pinguimImage = pinguimPuloRight
                    pygame.mixer.Sound.stop(walk)
                    pygame.mixer.Sound.play(pulo)
                direction = "right"
            
            #Procura pela tecla de seta para cima ser pressionada  
            elif not keys[pygame.K_LEFT] or not keys[pygame.K_RIGHT]:
                pygame.mixer.Sound.stop(walk)
            if keys[pygame.K_UP] and (upLadder or gameDone or winGame):
                # Se upLadder for True, move pinguim para cima 5 pixels
                if upLadder:
                    pinguimY = pinguimY - 5
                    
                    #Se a imagem do pinguim for diferente dele escalando, muda para ele escalando
                    if pinguimImage != pinguimClimb1:
                        pinguimImage = pinguimClimb1
            
            #Procura pela tecla de seta para baixo ser pressionada e só executa quando você pode descer por uma escada, e para selecionar
            if keys[pygame.K_DOWN] and (downLadder or gameDone or winGame):
                #Se downLadder for True, muda as coordenadas y do pinguim para descer
                if downLadder:
                    pinguimY = pinguimY + 5
                    
                    #Se a imagem do pinguim for diferente dele escalando, muda para ele escalando
                    if pinguimImage != pinguimClimb1:
                        pinguimImage = pinguimClimb1
            
            #lProcura pela barra de espaço ser pressionada e só pode fazer algo quando o pinguim já está pulando para a esquerda ou direita e você não está no meio de uma escada
            if keys[pygame.K_SPACE] and puloEsquerda == False and puloDireita == False and moveSides:
                #faz puloParado True
                puloParado = True
                
                #Se estiver virado para a esquerda, blit a imagem do pinguim pulando, virado para a direita
                if direction == "right":
                    pinguimImage = pinguimPuloRight
                    
                #se nao, blit o pinguim pulando e virado para a esquerda
                else:
                    pinguimImage = pinguimPuloLeft
            
        clock.tick(30) #30 e a taxa de quadro definida
        pygame.display.update() #jogo atualiza a cada loop 
        if inPlay: # Se inPlay for verdadeiro, a tela é constantemente redesenhada (animada). 
            redraw_screen() #a tela deve ser constantemente redesenhada - animação
        
        if startOutput:
            # Se startOutput for verdadeiro, indica que o início do jogo está sendo ativado.
            # Aqui, resetamos startOutput para False para garantir que essa transição ocorra apenas uma vez,
            # e definimos gameStart como True para iniciar o jogo.
            startOutput = False
            gameStart = True
        
        if winGameSceneOutput:
            # Se winGameSceneOutput for verdadeiro, indica que a cena de vitória está sendo ativada.
            # Aqui, resetamos winGameSceneOutput para False para garantir que essa transição ocorra apenas uma vez,
            # e definimos winGameSceneDone como True para indicar que a cena de vitória está concluída. 
            winGameSceneOutput = False
            winGameSceneDone = True
    pygame.quit() # Finaliza o módulo pygame após o término do jogo.                        

pygame.quit