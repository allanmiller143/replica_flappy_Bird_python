import pygame
import os
class Passaro:
    IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))), 
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))), 
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))
]
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 0
    TEMPO_ANIMACAO = 5
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
        
    def pular(self):
        self.velocidade = -8
        self.y += self.velocidade        
        
    def mover(self):
        #calcular o  deslocamento
        
        self.velocidade += 0.5  # Adiciona um valor constante à velocidade
        self.y += self.velocidade 
        # o angulo do passarro
        
        
        if(self.velocidade > 20):
            self.velocidade =20
        
        if(self.velocidade < 0): 
            if(self.angulo <self.ROTACAO_MAXIMA):
                self.VELOCIDADE_ROTACAO +=6.5
                self.angulo = self.VELOCIDADE_ROTACAO
        else:
            if(self.angulo > -self.ROTACAO_MAXIMA):
                self.VELOCIDADE_ROTACAO -=6.5
                self.angulo = self.VELOCIDADE_ROTACAO
                 
    def desenhar(self,tela):
        self.contagem_imagem += 1
        
        if(self.contagem_imagem < self.TEMPO_ANIMACAO):   
            self.imagem = self.IMGS[0]
        elif(self.contagem_imagem < self.TEMPO_ANIMACAO*2):
            self.imagem = self.IMGS[1] 
        elif(self.contagem_imagem < self.TEMPO_ANIMACAO*3):
            self.imagem = self.IMGS[2]
        elif(self.contagem_imagem < self.TEMPO_ANIMACAO*4):
            self.imagem = self.IMGS[1]  
        elif(self.contagem_imagem < self.TEMPO_ANIMACAO*5):
            self.imagem = self.IMGS[0]                     
            self.contagem_imagem = 0
            
            
        imagem_rotacionada = pygame.transform.rotate(self.imagem,self.angulo)
        centro_imagem = self.imagem.get_rect(topleft =( self.x,self.y)).center
        retangulo = imagem_rotacionada.get_rect(center = centro_imagem )   
        tela.blit(imagem_rotacionada,retangulo.topleft)
        
    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)    
            
                                                 