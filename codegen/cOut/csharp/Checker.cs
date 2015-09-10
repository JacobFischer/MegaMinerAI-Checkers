using System;
using System.Runtime.InteropServices;

/// <summary>
/// A checker on the game board.
/// </summary>
public class Checker
{
  public IntPtr ptr;
  protected int ID;
  protected int iteration;

  public Checker()
  {
  }

  public Checker(IntPtr p)
  {
    ptr = p;
    ID = Client.checkerGetId(ptr);
    iteration = BaseAI.iteration;
  }

  public bool validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.checkers.Length; i++)
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

  #region Commands
  /// <summary>
  /// Commands a checker to move to a new location.
  /// </summary>
  public bool move(int x, int y)
  {
    validify();
    return (Client.checkerMove(ptr, x, y) == 0) ? false : true;
  }
  #endregion

  #region Getters
  /// <summary>
  /// Unique Identifier
  /// </summary>
  public int Id
  {
    get
    {
      validify();
      int value = Client.checkerGetId(ptr);
      return value;
    }
  }

  /// <summary>
  /// The players id that controls this Checker.
  /// </summary>
  public int Owner
  {
    get
    {
      validify();
      int value = Client.checkerGetOwner(ptr);
      return value;
    }
  }

  /// <summary>
  /// The x coordinate of the checker.
  /// </summary>
  public int X
  {
    get
    {
      validify();
      int value = Client.checkerGetX(ptr);
      return value;
    }
  }

  /// <summary>
  /// The y coordinate of the checker.
  /// </summary>
  public int Y
  {
    get
    {
      validify();
      int value = Client.checkerGetY(ptr);
      return value;
    }
  }

  /// <summary>
  /// 1 if kinged,
  /// </summary>
  public int Kinged
  {
    get
    {
      validify();
      int value = Client.checkerGetKinged(ptr);
      return value;
    }
  }

  #endregion

  #region Properties
  #endregion
}
