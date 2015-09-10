import com.sun.jna.Pointer;

///A checker on the game board.
class Checker
{
  Pointer ptr;
  int ID;
  int iteration;
  public Checker(Pointer p)
  {
    ptr = p;
    ID = Client.INSTANCE.checkerGetId(ptr);
    iteration = BaseAI.iteration;
  }
  boolean validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.checkers.length; i++)
    {
      if(BaseAI.checkers[i].ID == ID)
      {
        ptr = BaseAI.checkers[i].ptr;
        iteration = BaseAI.iteration;
        return true;
      }
    }
    throw new ExistentialError();
  }

    //commands

  ///Commands a checker to move to a new location.
  boolean move(int x, int y)
  {
    validify();
    return (Client.INSTANCE.checkerMove(ptr, x, y) == 0) ? false : true;
  }

    //getters

  ///Unique Identifier
  public int getId()
  {
    validify();
    return Client.INSTANCE.checkerGetId(ptr);
  }
  ///The players id that controls this Checker.
  public int getOwner()
  {
    validify();
    return Client.INSTANCE.checkerGetOwner(ptr);
  }
  ///The x coordinate of the checker.
  public int getX()
  {
    validify();
    return Client.INSTANCE.checkerGetX(ptr);
  }
  ///The y coordinate of the checker.
  public int getY()
  {
    validify();
    return Client.INSTANCE.checkerGetY(ptr);
  }
  ///1 if kinged,
  public int getKinged()
  {
    validify();
    return Client.INSTANCE.checkerGetKinged(ptr);
  }

}
