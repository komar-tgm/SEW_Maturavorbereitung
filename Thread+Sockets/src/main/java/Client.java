import java.io.*;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class Client {
    public static void main(String[] args){
        try{
            Socket socket = new Socket("localhost", 4041);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter pw = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()),true);
            Scanner scanner = new Scanner(System.in);

            String nachricht;

            while (true){
                System.out.println("ENTER SOMETHING");
                nachricht = scanner.nextLine();

                pw.println(nachricht);
                System.out.println("SENT TO SERVER: "+nachricht);

                String serverText;
                if((serverText=in.readLine())!=null){
                    if(!serverText.equals("exit")){
                        System.out.println("RECEIVED FROM SERVER: "+serverText);
                    } else {
                        break;
                    }
                }
            }

        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
