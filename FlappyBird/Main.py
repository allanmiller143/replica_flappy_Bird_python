import pygame # biblioteca usada para criação de games em python 
import os  # biblioteca que permite integrar o codigo com os arquivos do pc
import Passaro
import Cano
import Chao
import time
import random

# passo 1: Definir as constantes do jogo, tamanho da tela, imagens usadas e fonte do texto 

LARGURA_TELA = 570
ALTURA_TELA = 680

# pygame.image.load = carrega a imagem do pc, os.path.join = acessa a pasta em que a imagem está


IMAGEM_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))


pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("arial",30)

def desenhar_tela(tela,passaro,canos,chao, pontos):
    tela.blit(IMAGEM_FUNDO,(0,0))
    passaro.desenhar(tela)
        
    for cano in canos:
        cano.desenhar(tela)   
               

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}",1,(255,255,255))
    tela.blit(texto,(LARGURA_TELA - 10 - texto.get_width(),10))
    chao.desenhar(tela)
    pygame.display.update()
    
 
def main():
    passaro = Passaro.Passaro(230, 350)
    chao = Chao.Chao(620)  # Usar Chao.Chao para referenciar a classe
    canos = [Cano.Cano(500,random.randrange(50,450) ),Cano.Cano(900,random.randrange(50,450) )]
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(40  )

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    passaro.pular()
 
       
        passaro.mover()

        chao.mover() 
        
        for cano in canos:
            cano.mover() 
            if cano.x + cano.CANO_BASE.get_width() < 0:
                cano.passou = False
                cano.x = 700
                cano.altura = random.randrange(50,450)
                cano.definir_altura( ) 
            
            if(cano.x + cano.CANO_TOPO.get_width() < passaro.x and cano.passou == False):
                cano.passou = True
                pontos += 1   
        
            if(cano.colidir(passaro)):
                tela.blit("FIM DE JOGO",(LARGURA_TELA/2,ALTURA_TELA/2))
                time.sleep(5)
  
                         
        desenhar_tela(tela, passaro, canos, chao, pontos)

    pygame.quit()
    quit()

main()



# criar um ambiente virtual

#passo1: python -m venv .\venv

# .\venv\Scripts\activate.bat
# pyinstaller --onefile -w para deixar executavel

