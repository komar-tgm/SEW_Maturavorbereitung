package Person;

import Oberteil.Oberteil;
import Schuh.Schuh;

public abstract class Person {
    Oberteil oberteil;
    Schuh schuh;

    public void showOberteil(){
        oberteil.showOberteil();
    }
    public void showSchuh(){
        schuh.showSchuh();
    }
    public void showOutfit(){
        oberteil.showOberteil();
        schuh.showSchuh();
    }

    public abstract void display();
}
