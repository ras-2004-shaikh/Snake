import pygame
from enum import Enum
pygame.init()

class Direction(Enum):
	top=(0,-1)
	right=(1,0)
	bottom=(0,1)
	left=(-1,0)

class HeadBlock:
	def __init__(self,nxt,pos,direction):
		self.pos=pos
		self.direction=direction
		self.nxt=nxt


class BodyBlock:
	def __init__(self,prev,nxt,pos):
		self.pos=pos
		self.prev=prev
		self.nxt=nxt

class TailBlock:
	def __init__(self,prev,pos):
		self.pos=pos
		self.prev=prev

class FoodBlock:
	def __init__(self,pos):
		self.pos=pos

class Snake:
	def __init__(self,pos,direction):
		self.pos=pos
		self.direction=direction



WIN=pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
CLOCK=pygame.time.Clock()

run=True
while run:
	CLOCK.tick(64)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		elif event.type==pygame.KEYDOWN:
			

