from PPlay.collision import *   
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

import os

img_dir = os.path.dirname(os.path.abspath(__file__)) + '/img/'

janela = Window(728, 410)
janela.set_title("Pong")
janela.draw_text("pong", 5, 5, 16,  (255,255,255), "Calibri", True)
fundo = GameImage(img_dir + "fundo.jpg")

teclado = Window.get_keyboard()
ponto1 = 0
ponto2 = 0


padvel = 200

#BOLA
bola = Sprite(img_dir + "bola.png", 1)
bola.x = janela.width/2 - bola.width/2 
bola.y = janela.height/2 - bola.height/2
velx = 290
vely = 290

#PAD1
pad1 = Sprite(img_dir + "pad.png", 1)
pad1.x = 5
pad1.y = janela.height/2 - pad1.height/2

#PAD2
pad2 = Sprite(img_dir + "pad.png", 1)
pad2.x = janela.width - pad2.width -5 
pad2.y = janela.height/2 - pad2.height/2

while (True):

    #CONTROLE DE VELOCIDADE DA BOLA
    bola.x = bola.x + velx * janela.delta_time()
    bola.y =  bola.y + vely * janela.delta_time()

    #MOVIEMTENA O PAD
    if teclado.key_pressed("w") and pad1.y >= 0:
        pad1.y -= padvel * janela.delta_time()
    if teclado.key_pressed("s") and pad1.y <= janela.height - pad1.height:
        pad1.y += padvel * janela.delta_time()
    if teclado.key_pressed("UP") and pad2.y >= 0:
        pad2.y -= padvel * janela.delta_time()
    if teclado.key_pressed("DOWN") and pad2.y <= janela.height - pad2.height:
        pad2.y += padvel * janela.delta_time()


    #COLISÃO PAD BOLA
    if(Collision.collided_perfect(bola, pad1)):
        velx = - velx
        bola.x = pad1.x + pad1.width + 1
        bola_center = bola.y + bola.height / 2
        pad_center = pad1.y + pad1.height / 2
        vely = (bola_center - pad_center) * 2

    if(Collision.collided_perfect(bola, pad2)):
        velx = - velx
        bola.x = pad2.x - bola.width - 1
        bola_center = bola.y + bola.height / 2
        pad_center = pad2.y + pad2.height / 2
        vely = (bola_center - pad_center) * 2

    #FISICA DA BOLA
    if bola.y >= 370 or bola.y <= -10:
        vely = -vely
    if bola.x >= 674:
        velx = -velx
        ponto1 += 1
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2

    if bola.x <= -24:
        velx = -velx
        ponto2 += 1
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2

    fundo.draw()
    janela.draw_text(f"JOGADOR 1 : {ponto1}", 35, 10, 16,  (255,255,255), "Calibri", True)
    janela.draw_text(f"JOGADOR 2 : {ponto2}", 600, 10, 16,  (255,255,255), "Calibri", True)
    bola.draw()
    pad1.draw()
    pad2.draw()
    janela.update()