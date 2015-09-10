# -*- python -*-

from library import library

from ExistentialError import ExistentialError

class GameObject(object):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration


##
class Player(GameObject):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.playerGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.players:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  #\cond
  def getId(self):
    self.validify()
    return library.playerGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getPlayerName(self):
    self.validify()
    return library.playerGetPlayerName(self._ptr)
  #\endcond
  ##Player's Name
  playerName = property(getPlayerName)

  #\cond
  def getTime(self):
    self.validify()
    return library.playerGetTime(self._ptr)
  #\endcond
  ##Time remaining, updated at start of turn
  time = property(getTime)

  #\cond
  def getYDirection(self):
    self.validify()
    return library.playerGetYDirection(self._ptr)
  #\endcond
  ##The direction your checkers must go along the y-axis until kinged
  yDirection = property(getYDirection)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "playerName: %s\n" % self.getPlayerName()
    ret += "time: %s\n" % self.getTime()
    ret += "yDirection: %s\n" % self.getYDirection()
    return ret

##A checker on the game board.
class Checker(GameObject):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.checkerGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.checkers:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  ##Commands a checker to move to a new location.
  def move(self, x, y):
    self.validify()
    return library.checkerMove(self._ptr, x, y)

  #\cond
  def getId(self):
    self.validify()
    return library.checkerGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getOwner(self):
    self.validify()
    return library.checkerGetOwner(self._ptr)
  #\endcond
  ##The players id that controls this Checker.
  owner = property(getOwner)

  #\cond
  def getX(self):
    self.validify()
    return library.checkerGetX(self._ptr)
  #\endcond
  ##The x coordinate of the checker.
  x = property(getX)

  #\cond
  def getY(self):
    self.validify()
    return library.checkerGetY(self._ptr)
  #\endcond
  ##The y coordinate of the checker.
  y = property(getY)

  #\cond
  def getKinged(self):
    self.validify()
    return library.checkerGetKinged(self._ptr)
  #\endcond
  ##1 if kinged,
  kinged = property(getKinged)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "owner: %s\n" % self.getOwner()
    ret += "x: %s\n" % self.getX()
    ret += "y: %s\n" % self.getY()
    ret += "kinged: %s\n" % self.getKinged()
    return ret
