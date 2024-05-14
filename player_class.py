import os

import pygame


class Player:
  def __init__(self,x,y,speed,window):
    self.alive=True
    self.import_player_assets()
    self.frame_index=0
    self.animation_speed=0.35
    self.image=self.animations["stand"][0]
    self.x=x
    self.y=y
    self.rect=self.image.get_rect(topleft=(x,y))
    self.speed=speed
    self.window=window
    self.jumping=False
    self.crouching=False
    self.jumpcount=0
    self.max_jump=14
    self.gravity=1.2
    self.ground_level=325
    self.state='running'
    
  def import_player_assets(self):
    self.animations={"run":["Run1.png","Run2.png"],
                     "crouch":["Crouch1.png","Crouch2.png"],
                     "jump":['Stand.png'],
                     "dead":["Dead.png"],
                     "stand":["Stand.png"]}
    for state in self.animations:
      for i in range(len(self.animations[state])):
        self.animations[state][i]=pygame.transform.scale_by(pygame.image.load(os.path.join("player_assets",self.animations[state][i])).convert_alpha(),2)
  
  def get_state(self):
    if not self.alive:
      state="dead"
    elif self.jumping:
      state="jump"
    elif self.crouching:
      state="crouch"
    else:
      state="run"
    return state
  
  def animate_player(self):
    self.state=self.get_state()
    animations=self.animations[self.state]
    self.frame_index+=self.animation_speed
    if self.frame_index>=len(animations):
      self.frame_index=0
    self.image=animations[int(self.frame_index)]
    
  def draw(self):
    self.animate_player()
    self.window.blit(self.image, self.rect)

  def jump(self):
    keys=pygame.key.get_pressed()
    self.y-=self.jumpcount
    self.y=min(self.ground_level,self.y)
    if self.y<self.ground_level:
      self.jumping=True
    else:
      self.jumping=False
    if self.jumping:
      self.jumpcount-=self.gravity
    elif keys[pygame.K_w]:
        self.jumpcount=self.max_jump
      
  def crouch(self):
    keys=pygame.key.get_pressed()
    if keys[pygame.K_s]:
      if self.jumping:
        self.jumpcount=min(self.jumpcount,-self.max_jump)
      else:
        self.crouching=True
    else:
      self.crouching=False
  
  def movements(self):
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
      self.x-=self.speed
    if keys[pygame.K_d]:
      self.x+=self.speed
    #can't jump when crouch
    self.crouch()
    if not self.crouching:
      self.jump()
    else:
      self.y=339 #crouch image is a litte higner, so need change y
    self.rect.x=self.x
    self.rect.y=self.y
  
  def update(self):
    self.movements()
