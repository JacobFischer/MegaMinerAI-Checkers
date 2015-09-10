using System;
using System.Runtime.InteropServices;

public class Client {
  [DllImport("client")]
  public static extern IntPtr createConnection();
  [DllImport("client")]
  public static extern int serverConnect(IntPtr connection, string host, string port);

  [DllImport("client")]
  public static extern int serverLogin(IntPtr connection, string username, string password);
  [DllImport("client")]
  public static extern int createGame(IntPtr connection);
  [DllImport("client")]
  public static extern int joinGame(IntPtr connection, int id, string playerType);

  [DllImport("client")]
  public static extern void endTurn(IntPtr connection);
  [DllImport("client")]
  public static extern void getStatus(IntPtr connection);

  [DllImport("client")]
  public static extern int networkLoop(IntPtr connection);

#region Commands
  [DllImport("client")]
  public static extern int checkerMove(IntPtr self, int x, int y);
#endregion

#region Accessors
  [DllImport("client")]
  public static extern int getBoardWidth(IntPtr connection);
  [DllImport("client")]
  public static extern int getBoardHeight(IntPtr connection);
  [DllImport("client")]
  public static extern int getTurnNumber(IntPtr connection);
  [DllImport("client")]
  public static extern int getPlayerID(IntPtr connection);
  [DllImport("client")]
  public static extern int getGameNumber(IntPtr connection);

  [DllImport("client")]
  public static extern IntPtr getPlayer(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getPlayerCount(IntPtr connection);
  [DllImport("client")]
  public static extern IntPtr getChecker(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getCheckerCount(IntPtr connection);
#endregion

#region Getters
  [DllImport("client")]
  public static extern int playerGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern IntPtr playerGetPlayerName(IntPtr ptr);
  [DllImport("client")]
  public static extern float playerGetTime(IntPtr ptr);
  [DllImport("client")]
  public static extern int playerGetYDirection(IntPtr ptr);

  [DllImport("client")]
  public static extern int checkerGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern int checkerGetOwner(IntPtr ptr);
  [DllImport("client")]
  public static extern int checkerGetX(IntPtr ptr);
  [DllImport("client")]
  public static extern int checkerGetY(IntPtr ptr);
  [DllImport("client")]
  public static extern int checkerGetKinged(IntPtr ptr);

#endregion

#region Properties
#endregion
}
