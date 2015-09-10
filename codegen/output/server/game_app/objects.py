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
    game = self.game
    if self.owner != game.playerID:
      return 'Turn {}: You cannot use the other player\'s checker {}. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)

    if game.checkerMoved:
      if game.checkerMoved != self:
        return 'Turn {}: You cannot move this checker as another already moved'.format(self.game.turnNumber)

    yOffset = 0
    yKinged = 0

    if self.owner == 0: # first player moves down
      yOffset = 1
      yKinged = game.boardHeight - 1
    else:
      yOffset = -1
      yKinged - 0

    dy = y - self.y
    dx = x - self.x

    if not self.kinged: # then jumping
      if (yOffset == 1 and dy < 1) or (yOffset == -1 and dy > -1):
        return 'Turn {}: moved in the wrong y direction'.format(self.game.turnNumber)

    jumped = None
    if abs(dx) == 2 and abs(dy) == 2: # jumping
      jumped = game.getCheckerAt(self.x + dx/2, self.y + dy/2)

      if not jumped:
        return 'Turn {}: Tried to jump nothing'.format(self.game.turnNumber)
      elif jumped.owner == self.owner:
        return 'Turn {}: You cannot jump your own checker'.format(self.game.turnNumber)
    elif abs(dx) == 1 and abs(dy) == 1: # then moving diag one
      if game.checkerMovedJumped:
        return 'Turn {}: current checker must jump again, not move diagonally'.format(self.game.turnNumber)
    else:
      return 'Turn {}: You cannot move: ({},{}) -> ({},{})'.format(self.game.turnNumber, self.x, self.y, x, y)

    # if we got here the move is valid!
    self.x = x
    self.y = y

    if self.y == yKinged:
      self.kinged = True

    game.checkerMoved = self

    if jumped:
      game.removeObject(jumped)

    return True

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

