//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef VC_STRUCTURES_H
#define VC_STRUCTURES_H

namespace client
{

struct Connection;
struct _Player;
struct _Checker;


struct _Player
{
  Connection* _c;
  int id;
  char* playerName;
  float time;
  int yDirection;
};
struct _Checker
{
  Connection* _c;
  int id;
  int owner;
  int x;
  int y;
  int kinged;
};

}

#endif
