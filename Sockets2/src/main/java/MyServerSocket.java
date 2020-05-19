import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * ServerSocket der nur 1 Client Socket gleichzeitig haben kann
 */
public class MyServerSocket {

    public static void main(String[] args) {
        try {
            //Initialisierung des Serversockets mittles Port
            ServerSocket serverSocket = new ServerSocket(4040);

            //Der Clientsocket wird akzeptiert
            Socket socket = serverSocket.accept();

            //Input und Outputstreams werden initialisiert
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter pw = new PrintWriter(socket.getOutputStream(),true);

            //Solange vom InputStream Zeilen kommen werden diese Zeilen bearbeitet
            String text;
            while ((text=bufferedReader.readLine())!=null){
                System.out.println("Client sent: "+text);
                //Wenn vom Client exit kommt wird ein exit zurückgeschickt
                if(!text.equals("exit")){
                    String reverseText = ReverseString.revers(text);
                    System.out.println(reverseText);
                    pw.println(reverseText);
                }else{
                    pw.println(text);
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
