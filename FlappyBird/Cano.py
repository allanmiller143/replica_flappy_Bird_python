import pygame
import os

class Cano:
    
    DISTANCIA = 150
    VELOCIDADE = 5
    
    def __init__(self,x,altura):
        self.x = x
        self.altura = altura
        self.posicao_cano_topo = 0
        self.posicao_cano_base = 0
        self.CANO_TOPO = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png"))) ,False,True)
        self.CANO_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png"))) 
        self.passou = False
        self.definir_altura()
        
    def definir_altura(self):
        self.posicao_cano_topo = self.altura - self.CANO_TOPO.get_height()
        self.posicao_cano_base = self.altura + self.DISTANCIA
        print(self.altura)
        
        
    def mover(self):
        self.x -= self.VELOCIDADE
        
    def desenhar(self,tela):
        tela.blit(self.CANO_TOPO,(self.x,self.posicao_cano_topo))
        tela.blit(self.CANO_BASE,(self.x,self.posicao_cano_base))

    def colidir(self,Passaro):
        passaro_mask = Passaro.get_mask()  
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)
        
        distancia_topo = (self.x - Passaro.x, self.posicao_cano_topo - round(Passaro.y))
        distancia_base = (self.x - Passaro.x, self.posicao_cano_base - round(Passaro.y))
        
        ponto_de_colisao_topo = passaro_mask.overlap(topo_mask, distancia_topo) 
        ponto_de_colisao_base = passaro_mask.overlap(base_mask, distancia_base)
        
        if(ponto_de_colisao_base or ponto_de_colisao_topo):
            return True
        else:
            return False  
                