// -*-c++-*-

#include "Checker.h"
#include "game.h"


namespace client
{

Checker::Checker(_Checker* pointer)
{
    ptr = (void*) pointer;
}

int Checker::id()
{
  return ((_Checker*)ptr)->id;
}

int Checker::owner()
{
  return ((_Checker*)ptr)->owner;
}

int Checker::x()
{
  return ((_Checker*)ptr)->x;
}

int Checker::y()
{
  return ((_Checker*)ptr)->y;
}

int Checker::kinged()
{
  return ((_Checker*)ptr)->kinged;
}


int Checker::move(int x, int y)
{
  return checkerMove( (_Checker*)ptr, x, y);
}



std::ostream& operator<<(std::ostream& stream,Checker ob)
{
  stream << "id: " << ((_Checker*)ob.ptr)->id  <<'\n';
  stream << "owner: " << ((_Checker*)ob.ptr)->owner  <<'\n';
  stream << "x: " << ((_Checker*)ob.ptr)->x  <<'\n';
  stream << "y: " << ((_Checker*)ob.ptr)->y  <<'\n';
  stream << "kinged: " << ((_Checker*)ob.ptr)->kinged  <<'\n';
  return stream;
}

}
