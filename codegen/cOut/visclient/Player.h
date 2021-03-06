// -*-c++-*-

#ifndef PLAYER_H
#define PLAYER_H

#include <iostream>
#include "vc_structures.h"


namespace client
{


class Player {
  public:
  void* ptr;
  Player(_Player* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///Player's Name
  char* playerName();
  ///Time remaining, updated at start of turn
  float time();
  ///The direction your checkers must go along the y-axis until kinged
  int yDirection();

  // Actions

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, Player ob);
};

}

#endif

