import pygame

class Life(object):
  def __init__(self, height, width):
    self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
    self.height = height
    self.width = width
    self.setup()

  def clear(self):
    self.screen.fill((0, 0, 0))

  def live(self, x, y):
    self.screen.set_at((x, y), (255, 255, 255))

  def die(self, x, y):
    self.screen.set_at((x, y), (0, 0, 0))

  def copy(self):
    self.prev_turn = self.screen.copy()

  def infinite(self, x, y):
    self.live(x, y + 5)
    self.live(x + 2, y +5)
    self.live(x + 2, y + 4)
    self.live(x + 4, y + 3)
    self.live(x + 4, y + 2)
    self.live(x + 4, y + 1)
    self.live(x + 6, y + 2)
    self.live(x + 6, y + 1)
    self.live(x + 6, y)
    self.live(x + 7, y + 1)

  def rpentomino(self, x, y):
    self.live(x + 1, y)
    self.live(x + 2, y)
    self.live(x + 1, y + 1)
    self.live(x, y + 1)
    self.live(x + 1, y + 2)
  
  def setup(self):
    self.rpentomino(int(self.width/4), int(self.height/4))
    self.infinite(int(3 * self.width/4), int(self.height/4))
    self.rpentomino(int(3 * self.width/4), int(3 * self.height/4))
    self.rpentomino(int(self.width/2), int(self.height/2))
    self.infinite(int(self.width/4), int(3 * self.height/4))




  def render(self):
    for x in range(0, self.width):
      for y in range(0, self.height):
        alive = 0
        isAlive = False
        for y1 in range(y - 1, y + 2):
          if y1 == self.height: y1 = 0
          if y1 == -1: y1 = self.height - 1
          for x1 in range(x - 1, x + 2):
            if x1 == self.width: x1 = 0
            if x1 == -1: x1 = self.width - 1  
            if self.prev_turn.get_at((x1, y1)) == (255, 255, 255, 255):
              if y1 == y and x1 == x: isAlive = True
              else: alive += 1
        
        #print("dead: %i, alive %i"%(dead, alive))
        if isAlive and (alive < 2 or alive > 3):
          self.die(x, y)
        if not isAlive and alive == 3:
          self.live(x, y)

            # if x % 20 == 0 and y % 20 == 0 and not (y1 == y and x1 == x):
            #   self.pixel(x1, y1)
            #   print(self.prev_turn.get_at((x, y)))


pygame.init()

r = Life(150, 150)

running = True
while running:
  #pygame.time.delay(50)
  r.copy()
  r.render()

  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False