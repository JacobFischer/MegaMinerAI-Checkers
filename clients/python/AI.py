#-*-python-*-
from BaseAI import BaseAI
from GameObject import *
from random import shuffle

class AI(BaseAI):
  """The class implementing gameplay logic."""
  @staticmethod
  def username():
    return "Shell AI"

  @staticmethod
  def password():
    return "password"

  ##This function is called once, before your first turn
  def init(self):
    self.checkersMap = [[False for y in range(self.getBoardWidth())] for x in range(self.getBoardHeight())]
    self.myCheckers = []

  def update(self):
    del self.myCheckers[:]

    for x in range(0, self.getBoardWidth()):
      for y in range(0, self.getBoardHeight()):
        self.checkersMap[x][y] = False

    for checker in self.checkers:
      self.checkersMap[checker.x][checker.y] = checker
      if checker.owner == self.getPlayerID():
        self.myCheckers.append(checker)

  ##This function is called once, after your last turn
  def end(self):
    pass

  ##This function is called each time it is your turn
  ##Return true to end your turn, return false to ask the server for updated information
  def run(self):
    self.update()

    checkers = list(self.myCheckers)

    shuffle(checkers)

    yDirection = 1 if self.getPlayerID() == 0 else -1

    for checker in checkers:
      neighbors = [
        {'x': checker.x + 1, 'y': checker.y + yDirection, 'requires jump': False},
        {'x': checker.x - 1, 'y': checker.y + yDirection, 'requires jump': False}
      ]

      if checker.kinged: # add the reversed y_direction neighbors to investigate moving to, because kinged peices can move in reverse
        neighbors.extend([
          {'x': checker.x + 1, 'y': checker.y - yDirection, 'requires jump': False},
          {'x': checker.x - 1, 'y': checker.y - yDirection, 'requires jump': False},
        ])

      shuffle(neighbors)
      while len(neighbors) > 0: # try to find a valid neighbor to move to
        neighbor = neighbors.pop()
        if neighbor['x'] >= self.getBoardWidth() or neighbor['x'] < 0 or neighbor['y'] >= self.getBoardHeight() or neighbor['y'] < 0:
          continue # because we can't use this neighbor as it is out of bounds

        if neighbor['requires jump']:
          checker.move(neighbor['x'], neighbor['y'])
          return 1
        else:
          jumping = self.checkersMap[neighbor['x']][neighbor['y']]
          if not jumping: # there's no checker there, so it's valid!
            checker.move(neighbor['x'], neighbor['y'])
            return 1
          elif jumping.owner != checker.owner: #there is one to jump so let's try to jump it
            if not neighbor['requires jump']: # then we have not already jumped to get here, so let's try to jump it
              dx = neighbor['x'] - checker.x
              dy = neighbor['y'] - checker.y

              neighbors.append({'x': neighbor['x'] + dx, 'y': neighbor['y'] + dy, 'requires jump': True})
    return 1 # shouldn't get here...

  def __init__(self, conn):
    BaseAI.__init__(self, conn)
