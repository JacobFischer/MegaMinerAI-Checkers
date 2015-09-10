# -*-python-*-

import os

from ctypes import *

try:
  if os.name == 'posix':
    library = CDLL("./libclient.so")
  elif os.name == 'nt':
    library = CDLL("./client.dll")
  else:
    raise Exception("Unrecognized OS: "+os.name)
except OSError:
  raise Exception("It looks like you didn't build libclient. Run 'make' and try again.")

# commands

library.createConnection.restype = c_void_p
library.createConnection.argtypes = []

library.serverConnect.restype = c_int
library.serverConnect.argtypes = [c_void_p, c_char_p, c_char_p]

library.serverLogin.restype = c_int
library.serverLogin.argtypes = [c_void_p, c_char_p, c_char_p]

library.createGame.restype = c_int
library.createGame.argtypes = [c_void_p]

library.joinGame.restype = c_int
library.joinGame.argtypes = [c_void_p, c_int, c_char_p]

library.endTurn.restype = None
library.endTurn.argtypes = [c_void_p]

library.getStatus.restype = None
library.getStatus.argtypes = [c_void_p]

library.networkLoop.restype = c_int
library.networkLoop.argtypes = [c_void_p]

#Functions
library.checkerMove.restype = c_int
library.checkerMove.argtypes = [c_void_p, c_int, c_int]

# accessors

#Globals
library.getBoardWith.restype = c_int
library.getBoardWith.argtypes = [c_void_p]

library.getBoardHeight.restype = c_int
library.getBoardHeight.argtypes = [c_void_p]

library.getTurnNumber.restype = c_int
library.getTurnNumber.argtypes = [c_void_p]

library.getPlayerID.restype = c_int
library.getPlayerID.argtypes = [c_void_p]

library.getGameNumber.restype = c_int
library.getGameNumber.argtypes = [c_void_p]

library.getPlayer.restype = c_void_p
library.getPlayer.argtypes = [c_void_p, c_int]

library.getPlayerCount.restype = c_int
library.getPlayerCount.argtypes = [c_void_p]

library.getChecker.restype = c_void_p
library.getChecker.argtypes = [c_void_p, c_int]

library.getCheckerCount.restype = c_int
library.getCheckerCount.argtypes = [c_void_p]

# getters

#Data
library.playerGetId.restype = c_int
library.playerGetId.argtypes = [c_void_p]

library.playerGetPlayerName.restype = c_char_p
library.playerGetPlayerName.argtypes = [c_void_p]

library.playerGetTime.restype = c_float
library.playerGetTime.argtypes = [c_void_p]

library.playerGetYDirection.restype = c_int
library.playerGetYDirection.argtypes = [c_void_p]

library.checkerGetId.restype = c_int
library.checkerGetId.argtypes = [c_void_p]

library.checkerGetOwner.restype = c_int
library.checkerGetOwner.argtypes = [c_void_p]

library.checkerGetX.restype = c_int
library.checkerGetX.argtypes = [c_void_p]

library.checkerGetY.restype = c_int
library.checkerGetY.argtypes = [c_void_p]

library.checkerGetKinged.restype = c_int
library.checkerGetKinged.argtypes = [c_void_p]


#Properties
