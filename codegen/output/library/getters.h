#ifndef GETTERS_H 
#define GETTERS_H
#include "structures.h"

#ifdef _WIN32
#define DLLEXPORT extern "C" __declspec(dllexport)
#else
#define DLLEXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

DLLEXPORT int playerGetId(_Player* ptr);
DLLEXPORT char* playerGetPlayerName(_Player* ptr);
DLLEXPORT float playerGetTime(_Player* ptr);
DLLEXPORT int playerGetYDirection(_Player* ptr);


DLLEXPORT int checkerGetId(_Checker* ptr);
DLLEXPORT int checkerGetOwner(_Checker* ptr);
DLLEXPORT int checkerGetX(_Checker* ptr);
DLLEXPORT int checkerGetY(_Checker* ptr);
DLLEXPORT int checkerGetKinged(_Checker* ptr);



#ifdef __cplusplus
}
#endif

#endif
