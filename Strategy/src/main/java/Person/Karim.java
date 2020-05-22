package Person;

import Oberteil.Jacke;
import Schuh.Continental;

public class Karim extends Person {
    public Karim(){
        this.oberteil = new Jacke();
        this.schuh = new Continental();
    }

    @Override
    public void display() {
        System.out.println("ICH BIN BABA");
    }
}
