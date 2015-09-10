from base import *
from matchUtils import *
from objects import *
import networking.config.config
from collections import defaultdict
from networking.sexpr.sexpr import *
import os
import itertools
import scribe
import jsonLogger

Scribe = scribe.Scribe

def loadClassDefaults(cfgFile = "config/defaults.cfg"):
  cfg = networking.config.config.readConfig(cfgFile)
  for className in cfg.keys():
    for attr in cfg[className]:
      setattr(eval(className), attr, cfg[className][attr])

class Match(DefaultGameWorld):
  def __init__(self, id, controller):
    self.id = int(id)
    self.controller = controller
    DefaultGameWorld.__init__(self)
    self.scribe = Scribe(self.logPath())
    if( self.logJson ):
      self.jsonLogger = jsonLogger.JsonLogger(self.logPath())
      self.jsonAnimations = []
      self.dictLog = dict(gameName = "Checkers", turns = [])
    self.addPlayer(self.scribe, "spectator")

    #TODO: INITIALIZE THESE!
    self.boardWidth = 8
    self.boardHeight = 8
    self.turnNumber = None
    self.playerID = -1
    self.gameNumber = id
    self.checkerMoved = None
    self.checkerMovedJumped = False

  #this is here to be wrapped
  def __del__(self):
    pass

  def addPlayer(self, connection, type="player"):
    connection.type = type
    if len(self.players) >= 2 and type == "player":
      return "Game is full"
    if type == "player":
      self.players.append(connection)
      try:
        self.addObject(Player, [connection.screenName, self.startTime, 1 if len(self.players) == 0 else -1])
      except TypeError:
        raise TypeError("Someone forgot to add the extra attributes to the Player object initialization")
    elif type == "spectator":
      self.spectators.append(connection)
      #If the game has already started, send them the ident message
      if (self.turn is not None):
        self.sendIdent([connection])
    return True

  def removePlayer(self, connection):
    if connection in self.players:
      if self.turn is not None:
        winner = self.players[1 - self.getPlayerIndex(connection)]
        self.declareWinner(winner, 'Opponent Disconnected')
      self.players.remove(connection)
    else:
      self.spectators.remove(connection)

  def start(self):
    if len(self.players) < 2:
      return "Game is not full"
    if self.winner is not None or self.turn is not None:
      return "Game has already begun"

    #TODO: START STUFF
    self.turn = self.players[-1]
    self.turnNumber = -1

    self._initCheckers()

    self.nextTurn()
    return True

  def _initCheckers(self):
    for y in range(0, self.boardHeight):
      for x in range(0, self.boardWidth):
        if self.isValidTile(x, y):
          ownerID = None

          if y < 3:
              ownerID = 0;
          elif y > 4:
              ownerID = 1;

          if ownerID != None:
            self.addObject(Checker, [ownerID, x, y, False])

  def isValidTile(self, x, y):
    return ((x + y)%2 == 1)

  def getCheckerAt(self, x, y):
    for checker in self.objects.checkers:
      if checker.x == x and checker.y == y:
        return checker

  def nextTurn(self):
    self.turnNumber += 1
    self.checkerMoved = None
    self.checkerMovedJumped = False
    if self.turn == self.players[0]:
      self.turn = self.players[1]
      self.playerID = 1
    elif self.turn == self.players[1]:
      self.turn = self.players[0]
      self.playerID = 0

    else:
      return "Game is over."

    for obj in self.objects.values():
      obj.nextTurn()

    self.checkWinner()
    if self.winner is None:
      self.sendStatus([self.turn] +  self.spectators)
    else:
      self.sendStatus(self.spectators)
    
    if( self.logJson ):
      self.dictLog['turns'].append(
        dict(
          boardWidth = self.boardWidth,
          boardHeight = self.boardHeight,
          turnNumber = self.turnNumber,
          playerID = self.playerID,
          gameNumber = self.gameNumber,
          Players = [i.toJson() for i in self.objects.values() if i.__class__ is Player],
          Checkers = [i.toJson() for i in self.objects.values() if i.__class__ is Checker],
          animations = self.jsonAnimations
        )
      )
      self.jsonAnimations = []

    self.animations = ["animations"]
    return True

  def checkWinner(self):
    onlyPlayerLeft = None
    twoPlayers = False
    checkers = [0, 0]
    kings = [0, 0]
    for checker in self.objects.checkers:
      checkers[checker.owner] += 1
      if checker.kinged:
        kings[checker.owner] += 1

      if onlyPlayerLeft == None:
        onlyPlayerLeft = checker.owner
      elif onlyPlayerLeft != checker.owner:
        twoPlayers = True

    if not twoPlayers: # then all the checkers are of one players
      self.declareWinner(self.players[onlyPlayerLeft], "has checkers remaining, other player does not")
      return

    if self.turnNumber >= self.turnLimit:
      if kings[0] > kings[1]:
        self.declareWinner(self.players[0], "Has more kings than player 1")
      elif kings[1] > kings[0]:
        self.declareWinner(self.players[1], "Has more kings than player 0")
      elif checkers[0] > checkers[1]:
        self.declareWinner(self.players[0], "Has more checkers than player 1")
      elif checkers[1] > checkers[0]:
        self.declareWinner(self.players[1], "Has more checkers than player 0")
      else:
        self.declareWinner(self.players[0], "Because I said so! You both have the same number of checkers!!!")


  def declareWinner(self, winner, reason=''):
    print "Player", self.getPlayerIndex(self.winner), "wins game", self.id
    self.winner = winner

    msg = ["game-winner", self.id, self.winner.user, self.getPlayerIndex(self.winner), reason]
    
    if( self.logJson ):
      self.dictLog["winnerID"] =  self.getPlayerIndex(self.winner)
      self.dictLog["winReason"] = reason
      self.jsonLogger.writeLog( self.dictLog )
    
    self.scribe.writeSExpr(msg)
    self.scribe.finalize()
    self.removePlayer(self.scribe)

    for p in self.players + self.spectators:
      p.writeSExpr(msg)
    
    self.sendStatus([self.turn])
    self.playerID ^= 1
    self.sendStatus([self.players[self.playerID]])
    self.playerID ^= 1
    self.turn = None
    self.objects.clear()

  def logPath(self):
    return "logs/" + str(self.id)

  @derefArgs(Checker, None, None)
  def move(self, object, x, y):
    return object.move(x, y, )


  def sendIdent(self, players):
    if len(self.players) < 2:
      return False
    list = []
    for i in itertools.chain(self.players, self.spectators):
      list += [[self.getPlayerIndex(i), i.user, i.screenName, i.type]]
    for i in players:
      i.writeSExpr(['ident', list, self.id, self.getPlayerIndex(i)])

  def getPlayerIndex(self, player):
    try:
      playerIndex = self.players.index(player)
    except ValueError:
      playerIndex = -1
    return playerIndex

  def sendStatus(self, players):
    for i in players:
      i.writeSExpr(self.status())
      i.writeSExpr(self.animations)
    return True


  def status(self):
    msg = ["status"]

    msg.append(["game", self.boardWidth, self.boardHeight, self.turnNumber, self.playerID, self.gameNumber])

    typeLists = []
    typeLists.append(["Player"] + [i.toList() for i in self.objects.values() if i.__class__ is Player])
    typeLists.append(["Checker"] + [i.toList() for i in self.objects.values() if i.__class__ is Checker])

    msg.extend(typeLists)

    return msg

  def addAnimation(self, anim):
    # generate the sexp
    self.animations.append(anim.toList())
    # generate the json
    if( self.logJson ):
      self.jsonAnimations.append(anim.toJson())
  


loadClassDefaults()

