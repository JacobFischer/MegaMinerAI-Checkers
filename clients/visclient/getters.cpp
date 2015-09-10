#include "getters.h"

namespace client
{

DLLEXPORT int playerGetId(_Player* ptr)
{
  return ptr->id;
}
DLLEXPORT char* playerGetPlayerName(_Player* ptr)
{
  return ptr->playerName;
}
DLLEXPORT float playerGetTime(_Player* ptr)
{
  return ptr->time;
}
DLLEXPORT int playerGetYDirection(_Player* ptr)
{
  return ptr->yDirection;
}
DLLEXPORT int checkerGetId(_Checker* ptr)
{
  return ptr->id;
}
DLLEXPORT int checkerGetOwner(_Checker* ptr)
{
  return ptr->owner;
}
DLLEXPORT int checkerGetX(_Checker* ptr)
{
  return ptr->x;
}
DLLEXPORT int checkerGetY(_Checker* ptr)
{
  return ptr->y;
}
DLLEXPORT int checkerGetKinged(_Checker* ptr)
{
  return ptr->kinged;
}

}
