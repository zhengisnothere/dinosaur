import pygame
import os
import random

class Spawner:
  def __init__(self, window, window_width, ground_speed, gorund_level):
    self.obstacle_types=['cactus1','cactus2','cactus3']
    self.obstacle_group = pygame.sprite.Group()
    self.window = window
    self.window_width = window_width
    self.ground_speed = ground_speed
    self.gorund_level = gorund_level
    self.load_obstacle_assets()
      
  def load_obstacle_assets(self):
    self.animations={"cactus1":["Cactus1.png"],
                     "cactus2":["Cactus2.png"],
                     "cactus3":['Cactus3.png']}
    for ot in self.animations:
      for i in range(len(self.animations[ot])):
        self.animations[ot][i]=pygame.transform.scale_by(pygame.image.load(os.path.join("obstacles_assets",self.animations[ot][i])).convert_alpha(),1.3)
      
  def spawn_obstacles(self):
    obstacle_type = random.choice(self.obstacle_types)
    obstacle_animation=self.animations[obstacle_type]
    self.obstacle_group.add(Obstacle(obstacle_animation, self.window, self.ground_speed, self.window_width, self.gorund_level, 0.25))

  def draw(self):
    self.obstacle_group.draw(self.window)

  def update(self):
    self.obstacle_group.update()
    self.obstacle_group.remove([obstacle for obstacle in self.obstacle_group if obstacle.rect.x <= -50])


class Obstacle(pygame.sprite.Sprite):
  def __init__(self, animation, window, speed, x, y, animation_speed):
    super().__init__()
    self.animation = animation
    self.image=animation[0]
    self.rect = self.image.get_rect(topleft=(x, y))
    self.speed = speed
    self.window = window
    self.frame_index=0
    self.animation_speed=animation_speed

  def animate_obstacle(self):
    self.frame_index+=self.animation_speed
    if self.frame_index>=len(self.animation):
      self.frame_index=0
    self.image=self.animation[int(self.frame_index)]
    
  def update(self):
    self.animate_obstacle()
    self.rect.x -= self.speed
