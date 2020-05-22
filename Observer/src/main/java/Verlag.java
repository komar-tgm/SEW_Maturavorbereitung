import java.util.ArrayList;

public class Verlag implements Subject{
    ArrayList<Observer> list;
    Zeitung zeitung;
    public Verlag(){
        this.list = new ArrayList<>();
        this.zeitung = new Zeitung();
    }
    @Override
    public void registerObserver(Observer observer) {
        list.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        list.remove(observer);
    }

    @Override
    public void updateObserver() {
        for (Observer observer:list){
            observer.getZeitungData();
        }
    }

    public void setZeitung(String name, String head, String text){
        this.zeitung.setName(name);
        this.zeitung.setHead(head);
        this.zeitung.setText(text);
        updateObserver();
    }
    public Zeitung getZeitung(){
        return this.zeitung;
    }
}
