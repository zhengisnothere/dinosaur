import os

import pygame


class Ground(pygame.sprite.Sprite):
  def __init__(self,x,y,speed,window):
    super().__init__()
    self.image=pygame.image.load(os.path.join("ground_assets","ground.png")).convert_alpha()
    self.image=pygame.transform.scale_by(self.image,0.45)
    self.x=x
    self.y=y
    self.rect=self.image.get_rect(topleft=(x,y))
    self.img_wid,self.img_hei=self.image.get_size()
    #694,18
    self.speed=speed
    self.window=window

  def draw(self):
    self.window.blit(self.image, self.rect)

  def scroll(self):
    self.x-=self.speed
    if self.x<=-self.img_wid:
      self.x+=3*self.img_wid
    self.rect.x=self.x
