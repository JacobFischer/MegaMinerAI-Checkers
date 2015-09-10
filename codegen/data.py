# -*- coding: iso-8859-1 -*-
from structures import *

aspects = ['timer']

gameName = "Checkers"

constants = [
  ]

modelOrder = ['Player', 'Checker']

globals = [
  Variable('boardWidth', int, 'The width of the board for X component of a checker.'),
  Variable('boardHeight', int, 'The height of the board for the Y component of a checker.'),
  Variable('turnNumber', int, 'The current turn number.'),
  Variable('playerID', int, 'The id of the current player.'),
  Variable('gameNumber', int, 'What number game this is for the server.')
]

playerData = [
  Variable('yDirection', int, 'The direction your checkers must go along the y-axis until kinged')
]

playerFunctions = []

#THIEF
Checker = Model('Checker',
  data = [
    Variable('owner', int, 'The players id that controls this Checker.'),
    Variable('x', int, 'The x coordinate of the checker.'),
    Variable('y', int, 'The y coordinate of the checker.'),
    Variable('kinged', int, '1 if kinged,'),
    ],
  doc='A checker on the game board.',
  functions=[
    Function('move', [Variable('x', int), Variable('y', int)],
    doc='Commands a checker to move to a new location.')
  ],
)

move = Animation('move',
  data=[
    Variable('sourceID', int),
    Variable('fromX', int),
    Variable('fromY', int),
    Variable('toX', int),
    Variable('toY', int)
  ],
)
