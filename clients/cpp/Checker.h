// -*-c++-*-

#ifndef CHECKER_H
#define CHECKER_H

#include <iostream>
#include "structures.h"


///A checker on the game board.
class Checker {
  public:
  void* ptr;
  Checker(_Checker* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///The players id that controls this Checker.
  int owner();
  ///The x coordinate of the checker.
  int x();
  ///The y coordinate of the checker.
  int y();
  ///1 if kinged,
  int kinged();

  // Actions
  ///Commands a checker to move to a new location.
  bool move(int x, int y);

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, Checker ob);
};

#endif

