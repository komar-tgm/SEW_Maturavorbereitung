import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class MySocket {
    public static void main(String[] args){
        try {
            Socket socket = new Socket("localhost",4040);
            Scanner scanner = new Scanner(System.in);
            PrintWriter pw=new PrintWriter(new OutputStreamWriter(socket.getOutputStream()),true);
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String text;
            while (true){
                System.out.println("Enter Text");
                text=scanner.nextLine();
                pw.println(text);
                System.out.println(text + " SENT");
                String serverText;
                if ((serverText=bufferedReader.readLine())!=null){
                    if(!serverText.equals("exit")){
                        System.out.println(serverText);
                    } else{
                        break;
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
