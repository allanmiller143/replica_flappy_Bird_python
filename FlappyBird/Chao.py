import pygame 
import os
class Chao:
    
    VELOCIDADE = 5
    LARGURA = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png"))).get_width()
    IMAGEM = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png"))) 
    
    def __init__(self,y):
        self.y = y
        self.x_primeiro_chao = 0
        self.x_segundo_chao = self.LARGURA
        
    def mover(self):
        self.x_primeiro_chao -= self.VELOCIDADE
        self.x_segundo_chao -= self.VELOCIDADE
        
        if(self.x_primeiro_chao + self.LARGURA < 0):
            self.x_primeiro_chao = self.LARGURA
            
        if(self.x_segundo_chao + self.LARGURA < 0):
            self.x_segundo_chao = self.LARGURA +10
            
    def desenhar(self,tela):
        tela.blit(self.IMAGEM,(self.x_primeiro_chao,self.y))
        tela.blit(self.IMAGEM,(self.x_segundo_chao,self.y))       
        
            
        