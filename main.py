import sys

import pygame
import random

from ground_class import Ground
from player_class import Player
from obstacles_class import Spawner
pygame.init()

class Game_Manager:
  def __init__(self):
    self.window_width=800
    self.window_height=400
    self.window=pygame.display.set_mode((self.window_width,self.window_height), pygame.DOUBLEBUF)
    pygame.display.set_caption('the last dinosaur')
    self.player=Player(100, 300,6,self.window)
    ground_wid=694
    ground_speed=12
    self.grounds=pygame.sprite.Group()
    for i in range(-1,2):
      self.grounds.add(Ground(i*ground_wid,350,ground_speed,self.window))
    self.spawner=Spawner(self.window, self.window_width, ground_speed, 325)
    self.clock=pygame.time.Clock()
    self.last_spawn_time=0
    self.spawn_interval=0

  def draw_text(self,x,y,size,text):
    font=pygame.font.Font(None,size)
    text_surface=font.render(text,True,(0,0,0))
    self.window.blit(text_surface,(x,y))
    
  def draw(self):
    self.window.fill((255,255,255))
    self.draw_text(0,0,15,str(int(self.clock.get_fps())))
    self.grounds.draw(self.window)
    self.spawner.draw()
    self.player.draw()
    pygame.display.update()
    
  def ground_scroll(self):
    for g in self.grounds:
      g.scroll()

  def try_spawn_obstacles(self):
    this_spawn_time=pygame.time.get_ticks()
    if this_spawn_time-self.last_spawn_time>=self.spawn_interval:
      self.spawner.spawn_obstacles()
      self.last_spawn_time=this_spawn_time
      self.spawn_interval=random.randint(800, 1000)

  def update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    self.try_spawn_obstacles()
    self.ground_scroll()
    self.spawner.update()
    self.player.update()
    
    self.draw()
    self.clock.tick(30)

game_manager=Game_Manager()

while True:
  game_manager.update()
