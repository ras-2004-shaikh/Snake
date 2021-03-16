import pygame
from enum import Enum
import random
pygame.init()

class Direction(Enum):
	top=(0,-1)
	right=(1,0)
	bottom=(0,1)
	left=(-1,0)


class SnakeBlock:
	def __init__(self,pos):
		self.pos=pos			
	def draw(self,size):
		pygame.draw.rect(WIN,(255,255,255),self.pos+size)
	def move(self,new):
		new=(new[0]%500,new[1]%500)
		self.pos=new

class FoodProducer:
	producers=[]
	def __init__(self,rect,size=10):
		self.rect=rect
		self.size=size
		self.food=self.generateFood()
		FoodProducer.producers.append(self)
	def eaten(self):
		del self.food
		self.food=self.generateFood()
	def generateFood(self):
		ch=True
		while ch:
			foodx=random.randint(self.rect[0],self.rect[2])
			foody=random.randint(self.rect[1],self.rect[3])
			ch=False
			for producer in FoodProducer.producers:
				if producer is not self and producer.food.pos==(foodx*self.size,foody*self.size):
					ch=True
					break
			for player in players:
				for part in player.parts:
					if part.pos==(foodx*self.size,foody*self.size):
						ch=True
						break
				if ch:break
		food=FoodBlock((foodx*self.size,foody*self.size),(self.size,self.size),self)
		return food
	def draw(self):
		self.food.draw()




class FoodBlock:
	def __init__(self,pos,size,producer):
		self.pos=pos
		self.size=size
		self.producer=producer
	def draw(self):
		pygame.draw.rect(WIN,(200,0,0),self.pos+self.size)

class Snake:
	def __init__(self,pos,direction,size=10,control=(pygame.K_UP,pygame.K_RIGHT,pygame.K_DOWN,pygame.K_LEFT)):
		self.pos=pos
		self.direction=direction
		self.size=(size,size)
		self.parts=[]
		self.head=SnakeBlock(pos)
		dir_val=self.direction.value
		tail_pos=tuple(p-size*d for p,d in zip(pos,dir_val))
		tail=SnakeBlock(tail_pos)
		self.parts.insert(0,tail)
		self.goto=self.direction
		self.control=control
		self.killed=False
	def eventManager(self,key):
		if key in self.control:
			index=self.control.index(key)
			if index==0 and self.direction!=Direction.bottom:self.direction=Direction.top
			elif index==1 and self.direction!=Direction.left:self.direction=Direction.right
			elif index==2 and self.direction!=Direction.top:self.direction=Direction.bottom
			elif index==3 and self.direction!=Direction.right:self.direction=Direction.left
	def move(self,tickc):
		for producer in FoodProducer.producers:
			if producer.food.pos==self.head.pos:
				producer.eaten()
				self.parts.append(SnakeBlock((self.parts[-1].pos)))
		if tickc == 0:
			prev_pos=self.head.pos
			new_pos=tuple((h+self.size[0]*d)%500 for h,d in zip(prev_pos,self.direction.value))
			for part in self.parts[:-1]:
				if new_pos==part.pos:
					self.killed=True
			self.head.move(new_pos)
			for block in self.parts:
				p_pos=block.pos
				block.move(prev_pos)
				prev_pos=p_pos
	def draw(self):
		if not self.killed:
			self.head.draw(self.size)
			for part in self.parts:
				part.draw(self.size)




WIN=pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
CLOCK=pygame.time.Clock()
tickc=-1

player=Snake((60,60),Direction.right,size=20)
players=[player]
FoodProducer((0,0,24,24),size=20)
run=True
key_events=[]
while run:
	CLOCK.tick(64)
	tickc+=1
	tickc%=7
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		elif event.type==pygame.KEYDOWN:
			key_events.append(event.key)
	if tickc==0 and key_events:
		player.eventManager(key_events.pop(0))
	WIN.fill((0,0,0))
	player.draw()
	for producer in FoodProducer.producers:
		producer.draw()
	player.move(tickc)
	pygame.display.update()

