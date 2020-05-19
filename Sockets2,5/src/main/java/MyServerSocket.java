import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Serversocket Klasse die mehrere Clients haben kann durch Threads
 */
public class MyServerSocket implements Runnable{
    private Socket socket;
    public MyServerSocket(Socket socket){
        this.socket=socket;
    }

    /**
     * Alles was in der Main Methode war kommt jetzt in die run Methode
     */
    public void run(){
        try (BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter pw = new PrintWriter(socket.getOutputStream(),true)){

            String text;
            while ((text=bufferedReader.readLine())!=null){
                System.out.println("Client sent: "+text);
                if(!text.equals("exit")){
                    String reverseText = ReverseString.revers(text);
                    System.out.println("Server will send: "+reverseText);
                    pw.println("Server sent: "+reverseText);
                }
                else{
                    pw.println(text);
                    break;
                }
            }
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        //Hier werden nun die Clients akzeptiert
        try (ServerSocket serverSocket = new ServerSocket(4040)) {
            while (true){
                //Für jeden Client wird ein neuer Thread gestartet
                new Thread(new MyServerSocket(serverSocket.accept())).start();
                //Implements Runnable erfordert ein eigenes Thread Objekt mit der Klasse als Parameter
                //Extends Thread kann die start() Methode direkt auf die Klasse aufrufen
                //z.B. new MyServerSocket(serverSocket.accept()).start()
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
