class Player(object):
  game_state_attributes = ['id', 'playerName', 'time', 'yDirection']
  def __init__(self, game, id, playerName, time, yDirection):
    self.game = game
    self.id = id
    self.playerName = playerName
    self.time = time
    self.yDirection = yDirection
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.playerName, self.time, self.yDirection, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, playerName = self.playerName, time = self.time, yDirection = self.yDirection, )
  
  def nextTurn(self):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class Checker(object):
  game_state_attributes = ['id', 'owner', 'x', 'y', 'kinged']
  def __init__(self, game, id, owner, x, y, kinged):
    self.game = game
    self.id = id
    self.owner = owner
    self.x = x
    self.y = y
    self.kinged = kinged
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.owner, self.x, self.y, self.kinged, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, owner = self.owner, x = self.x, y = self.y, kinged = self.kinged, )
  
  def nextTurn(self):
    pass

  def move(self, x, y):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)


# The following are animations and do not need to have any logic added
class MoveAnimation:
  def __init__(self, sourceID, fromX, fromY, toX, toY):
    self.sourceID = sourceID
    self.fromX = fromX
    self.fromY = fromY
    self.toX = toX
    self.toY = toY

  def toList(self):
    return ["move", self.sourceID, self.fromX, self.fromY, self.toX, self.toY, ]

  def toJson(self):
    return dict(type = "move", sourceID = self.sourceID, fromX = self.fromX, fromY = self.fromY, toX = self.toX, toY = self.toY)

