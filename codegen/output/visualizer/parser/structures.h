//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef STRUCTURES_H
#define STRUCTURES_H

#include <iostream>
#include <vector>
#include <map>
#include <string>

#include "smartpointer.h"

namespace parser
{

const int MOVE = 0;

struct Player
{
  int id;
  char* playerName;
  float time;
  int yDirection;

  friend std::ostream& operator<<(std::ostream& stream, Player obj);
};

struct Checker
{
  int id;
  int owner;
  int x;
  int y;
  int kinged;

  friend std::ostream& operator<<(std::ostream& stream, Checker obj);
};


struct Animation
{
  int type;
};

struct move : public Animation
{
  int sourceID;
  int fromX;
  int fromY;
  int toX;
  int toY;

  friend std::ostream& operator<<(std::ostream& stream, move obj);
};


struct AnimOwner: public Animation
{
  int owner;
};

struct GameState
{
  std::map<int,Player> players;
  std::map<int,Checker> checkers;

  int boardWidth;
  int boardHeight;
  int turnNumber;
  int playerID;
  int gameNumber;

  std::map< int, std::vector< SmartPointer< Animation > > > animations;
  friend std::ostream& operator<<(std::ostream& stream, GameState obj);
};

struct Game
{
  std::vector<GameState> states;
  std::string players[2];
  int winner;
	std::string winReason;

  Game();
};

} // parser

#endif
