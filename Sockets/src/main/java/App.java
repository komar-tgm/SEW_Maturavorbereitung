import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

/**
 * Eine simple Application die sich mit einem Server verbindet
 * und die aktuelle Zeit ausgibt
 */
public class App {

    public static void main(String[] args) {
        //Socket wird im try Block initialisiert
        try (Socket socket = new Socket("time.nist.gov",13)){

            //BufferedReader liest mittels InputStreamReader den Inputstream des Sockets
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String time;
            //Solange der Reader Zeilen besitzt, werden die Zeilen ausgegeben
            while ((time = bufferedReader.readLine())!=null){
                System.out.println(time);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
