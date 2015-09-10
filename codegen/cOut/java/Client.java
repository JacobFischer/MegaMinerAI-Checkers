import com.sun.jna.Library;
import com.sun.jna.Pointer;
import com.sun.jna.Native;

public interface Client extends Library {
  Client INSTANCE = (Client)Native.loadLibrary("client", Client.class);
  Pointer createConnection();
  boolean serverConnect(Pointer connection, String host, String port);

  boolean serverLogin(Pointer connection, String username, String password);
  int createGame(Pointer connection);
  int joinGame(Pointer connection, int id, String playerType);

  void endTurn(Pointer connection);
  void getStatus(Pointer connection);

  int networkLoop(Pointer connection);


    //commands
  int checkerMove(Pointer object, int x, int y);

    //accessors
  int getBoardWith(Pointer connection);
  int getBoardHeight(Pointer connection);
  int getTurnNumber(Pointer connection);
  int getPlayerID(Pointer connection);
  int getGameNumber(Pointer connection);

  Pointer getPlayer(Pointer connection, int num);
  int getPlayerCount(Pointer connection);
  Pointer getChecker(Pointer connection, int num);
  int getCheckerCount(Pointer connection);


    //getters
  int playerGetId(Pointer ptr);
  String playerGetPlayerName(Pointer ptr);
  float playerGetTime(Pointer ptr);
  int playerGetYDirection(Pointer ptr);

  int checkerGetId(Pointer ptr);
  int checkerGetOwner(Pointer ptr);
  int checkerGetX(Pointer ptr);
  int checkerGetY(Pointer ptr);
  int checkerGetKinged(Pointer ptr);


    //properties

}
