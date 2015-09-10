using System;
using System.Runtime.InteropServices;

/// <summary>
/// This class implements most the code an AI would need to interface with the lower-level game code.
/// AIs should extend this class to get a lot of builer-plate code out of the way. The provided AI class does just that.
/// </summary>
public abstract class BaseAI
{
  public static Player[] players;
  public static Checker[] checkers;

  IntPtr connection;
  public static int iteration;
  bool initialized;

  public BaseAI(IntPtr c)
  {
    connection = c;
  }

  /// <summary>
  /// Make this your username, which should be provided.
  /// </summary>
  /// <returns>Returns the username of the player.</returns>
  public abstract String username();

  /// <summary>
  /// Make this your password, which should be provided.
  /// </summary>
  /// <returns>Returns the password of the player.</returns>
  public abstract String password();

  /// <summary>
  /// This is run once on turn one before run().
  /// </summary>
  public abstract void init();

  /// <summary>
  /// This is run every turn.
  /// </summary>
  /// <returns>
  /// Return true to end turn, false to resynchronize with the 
  /// server and run again.
  /// </returns>
  public abstract bool run();

  /// <summary>
  /// This is run once after your last turn.
  /// </summary>
  public abstract void end();

  /// <summary>
  /// Synchronizes with the server, then calls run().
  /// </summary>
  /// <returns>
  /// Return true to end turn, false to resynchronize with the 
  /// server and run again.
  /// </returns>
  public bool startTurn()
  {
    int count = 0;
    iteration++;

    count = Client.getPlayerCount(connection);
    players = new Player[count];
    for(int i = 0; i < count; i++)
      players[i] = new Player(Client.getPlayer(connection, i));

    count = Client.getCheckerCount(connection);
    checkers = new Checker[count];
    for(int i = 0; i < count; i++)
      checkers[i] = new Checker(Client.getChecker(connection, i));

    if(!initialized)
    {
      initialized = true;
      init();
    }

    return run();
  }

  /// <summary>
  /// The width of the board for X component of a checker.
  /// </summary>
  /// <returns>Returns the width of the board for X component of a checker.</returns>
  public int boardWith()
  {
    int value = Client.getBoardWith(connection);
    return value;
  }

  /// <summary>
  /// The height of the board for the Y component of a checker.
  /// </summary>
  /// <returns>Returns the height of the board for the Y component of a checker.</returns>
  public int boardHeight()
  {
    int value = Client.getBoardHeight(connection);
    return value;
  }

  /// <summary>
  /// The current turn number.
  /// </summary>
  /// <returns>Returns the current turn number.</returns>
  public int turnNumber()
  {
    int value = Client.getTurnNumber(connection);
    return value;
  }

  /// <summary>
  /// The id of the current player.
  /// </summary>
  /// <returns>Returns the id of the current player.</returns>
  public int playerID()
  {
    int value = Client.getPlayerID(connection);
    return value;
  }

  /// <summary>
  /// What number game this is for the server.
  /// </summary>
  /// <returns>Returns what number game this is for the server.</returns>
  public int gameNumber()
  {
    int value = Client.getGameNumber(connection);
    return value;
  }
}
